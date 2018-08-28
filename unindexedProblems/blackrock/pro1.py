import sys
def exchange(need, pay):
	"""
		This gives the changes for customers
	"""
	if need > pay:
		return "ERROR"
	elif need == pay:
		return "ZERO"
	else:
		rep = {0.01:"PENNY",0.05:"NICKEL",0.10:"DIME",0.25:"QUARTER",\
		0.50:"HALF DOLLAR", 1.00:"ONE",2.00:"TWO",5.00:"FIVE",10.00:"TEN",\
		20.00:"TWENTY", 50.00:"FIFTY",100.00:"ONE HUNDRED"}
		stack = [0.01,0.05,0.10,0.25,0.5,1.0,2.0,5.0,10.0,20.0,50.0,100.0]
		res = ""
		diff = pay - need
		def helper(diff, rep, stack, result):
			if abs(diff) < 1e-5:
				return result
			else:
				while stack:
					print diff, stack
					candidate = stack[-1]
					if candidate <= diff:
						return ","+rep[candidate] + helper(diff-candidate, rep, stack, result)
					else:
						stack.pop()
		return helper(diff, rep, stack, res)
		
line = "24;300.04"
money = line.split(";")
print exchange(float(money[0]), float(money[1]))

