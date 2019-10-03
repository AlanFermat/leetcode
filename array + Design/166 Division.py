def divide(numerator, denominator):
	if denominator == 1:
		return str(numerator)
	res = ""
	if numerator * denominator < 0 :
		res = "-"
		numerator = abs(numerator)
		denominator = abs(denominator)
	divisor = numerator // denominator
	remainder = numerator % denominator
	if not remainder:
		return res + str(divisor)
	res += str(divisor)
	res += "."
	seen_divisor = {}
	digits = []
	idx = 0
	while remainder:
		next_num = remainder * 10
		next_divisor = next_num // denominator
		next_rem  = next_num % denominator
		if (next_divisor, next_rem) not in seen_divisor:
			digits.append(str(next_divisor))
			seen_divisor[(next_divisor, next_rem)] = idx
			remainder = next_rem
			idx += 1
		else:
			not_rec_digits = ''.join(digits[:seen_divisor[(next_divisor, next_rem)]])
			rec_digits = '(' + ''.join(digits[seen_divisor[(next_divisor, next_rem)]:]) + ')'
			res += not_rec_digits + rec_digits
			return res
	not_rec_digits = ''.join(digits)
	res += not_rec_digits
	return res

print (divide(-50, 8))







