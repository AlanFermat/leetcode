import json
from collections import defaultdict as dd
class MarkingPositionMonitor(object):
	"""docstring for MarkingPositionMonitor"""
	def __init__(self):
		self.data = dd(dict)
		self.order = dd(str)
		self.marking = 0
		self.symbol_marking = dd(int)

	### 0: firm send request to new stock
	### 1: order ack
	### 2: try to cancel
	### 3: cancel ack
	### 4: order reject
	### 5: cancel reject
	### 6: fill


	### self.data is in the form time, movable quantity, fixed quantity, status, id


	def NEW(self, info):
		if info["side"] == "SELL":
			self.data[info["symbol"]][info["order_id"]] = [info["time"],int(info["quantity"]), 0,"SELL",0]
			self.order[info["order_id"]] = info["symbol"]
			self.symbol_marking[info["symbol"]] -= info["quantity"]
		if info["side"] == "BUY":
			self.data[info["symbol"]][info["order_id"]] = [info["time"],int(info["quantity"]), 0,"BUY",0]
			self.order[info["order_id"]] = info["symbol"]
		

	def CANCEL(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0]:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 2
			if self.data[order_symbol][order_id][-2] == "BUY":
				self.symbol_marking[order_symbol] -= self.data[order_symbol][order_id][1]
				self.data[order_symbol][order_id][1] = 0



	def ORDER_ACK(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0] and self.data[order_symbol][order_id][-1] == 0:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 1


	def ORDER_REJECT(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0] and self.data[order_symbol][order_id][-1] == 0:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 4
			del self.symbol_marking[order_symbol] 

	def CANCEL_ACK(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0] and self.data[order_symbol][order_id][-1] == 2:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 3
			del self.symbol_marking[order_symbol] 

	def CANCEL_REJECT(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0] and self.data[order_symbol][order_id][-1] == 2:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 5
			if self.data[order_symbol][order_id][-2] == "BUY":
				self.symbol_marking[order_symbol] += self.data[order_symbol][order_id][1]

	def FILL(self, info):
		order_id = info["order_id"]
		order_symbol = self.order[order_id]
		if info["time"] > self.data[order_symbol][order_id][0] and self.data[order_symbol][order_id][-1] == 1:
			self.data[order_symbol][order_id][0] = info["time"]
			self.data[order_symbol][order_id][-1]= 6
			if self.data[order_symbol][order_id][-2] == "BUY":
				self.data[order_symbol][order_id][1] = info["remaining_quantity"]
				self.data[order_symbol][order_id][2] = info["filled_quantity"]
				self.symbol_marking[order_symbol] += self.data[order_symbol][order_id][2]
			if self.data[order_symbol][order_id][-2] == "SELL":
				self.data[order_symbol][order_id][1] = info["remaining_quantity"]
				self.data[order_symbol][order_id][2] = info["filled_quantity"]



	def on_event(self, message):
		info = json.loads(message)
		msg = info["type"]
		if msg == "NEW":
			self.NEW(info)
		if msg == "CANCEL":
			self.CANCEL(info)
		if msg == "ORDER_ACK":
			self.ORDER_ACK(info)
		if msg == "ORDER_REJECT":
			self.ORDER_REJECT(info)
		if msg == "FILL":
			self.FILL(info)
		if msg == "CANCEL_ACK":
			self.CANCEL_ACK(info)
		if msg == "CANCEL_REJECT":
			self.CANCEL_REJECT(info)
		if not self.symbol_marking.values():
			print 0
			return 
		self.marking = min(self.symbol_marking.values())
		print self.marking
		# print self.data



omm = MarkingPositionMonitor()
f = open("input.txt","r")
for line in f:
	message = line
	print omm.data
	omm.on_event(message)






