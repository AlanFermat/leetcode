def translate(num):
	def one(d):
		mapping = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
		return mapping[d]

	def two(d):
		mapping = {10:"Ten", 11: "Eleven", 12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen", 16:"Sixteen",\
					17: "Seventeen", 18:"Eighteen",19:"Nineteen",2: "Twenty",3:"Thrity",4:"Forty",\
					5:"Fifty",6:"Sixty", 7:"Seventy",8:"Eighty",9:"Ninety"}
		if d < 20:
			return mapping[d]
		else:
			if d % 10 == 0:
				return mapping[d // 10] 
			else:
				return mapping[d//10] + " "+ one(d%10)
	def three(d):
		h = d // 100
		remain = d % 100
		if remain > 9:
			return one(h) + " " + "Hundred" + " " + two(remain)
		elif remain > 0 and remain < 10:
			return one(h) + " " + "Hundred" + " " + one(remain)
		else:
			return one(h) + " " + "Hundred"



	unit = ["Billion","Million", "Thousand"]
	if num < 10:
		return one(num)
	if 9< num < 100:
		return two(num)
	if 99 < num < 1000:
		return three(num)
	b = num // 1000000000
	rb = num % 1000000000
	if b > 0:
		if rb > 0:
			return translate(b) + " " + unit[0] + " " + translate(rb)
		else:
			return translate(b) + " " + unit[0]
	m = num // 1000000
	rm = num % 1000000
	if m > 0:
		if rm > 0:
			return translate(m) + " " + unit[1] + " " + translate(rm)
		else:
			return translate(m) + " " + unit[1]
	t = num // 1000
	rt = num % 1000
	if t > 0:
		if rt > 0:
			return translate(t) + " " + unit[2] + " " + translate(rt)
		else:
			return translate(t) + " " + unit[2] 
	
num = 135000000
print (translate(num))









