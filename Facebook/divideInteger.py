def divide(self, dividend, divisor):
	"""
	:type dividend: int
	:type divisor: int
	:rtype: int
	"""
	positive = (dividend < 0) is (divisor < 0)
	res = 0
	dividend = abs(dividend)
	divisor = abs(divisor)
	while dividend >= divisor:
		temp = divisor
		quotient = 1
		while dividend >= temp:
			dividend -= temp
			res += quotient
			quotient <<= 1
			temp <<= 1
	if not positive:
		res = -res
	return res