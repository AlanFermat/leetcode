def divide(numerator, denominator):
	if denominator == 0:
		return
	if denominator == 1:
		return str(numerator)
	if numerator * denominator < 0:
		res = "-"
		numerator = abs(numerator)
		denominator = abs(denominator)
	else:
		res = ""
	res += str(numerator // denominator)
	remainder = numerator % denominator
	if remainder == 0:
		return res
	res += "."
	seen_divisor = {}
	idx = 0
	digits = []
	while remainder:
		next_num = remainder * 10
		divisor = next_num // denominator
		next_rem = next_num % denominator
		if seen_divisor.get((divisor, next_rem)) is None:
			seen_divisor[(divisor, next_rem)] = idx
			remainder = next_rem
			digits.append(str(divisor))
			idx += 1
		else:
			single_part = ''.join(digits[:seen_divisor[(divisor, next_rem)]])
			repeat_part = '(' + ''.join(digits[seen_divisor[(divisor, next_rem)]:]) + ')'
			return res + single_part + repeat_part
	single_part = ''.join(digits)
	return res + single_part

print (divide(11, 7))







