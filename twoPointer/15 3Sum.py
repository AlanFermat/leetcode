# Given an array S of n integers, are there elements a, b, c in S 
# such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

def threesum(arr):
	result = []
	n = len(arr)
	if n < 3:
		return []
	elif n == 3:
		if sum(arr) == 0:
			return [arr]
		else:
			return []
	else:
		arr.sort()
		for i in range(n-2):
			j = i+1
			k = n-1
			if i > 0 and arr[i] == arr[i-1]:
				continue
			else:
				while j < k:
					ttl = arr[i] + arr[j] + arr[k]
					if ttl > 0:
						k -= 1
					elif ttl < 0:
						j += 1
					else:
						result.append([arr[i],arr[j],arr[k]])
						while j < k and arr[j] == arr[j+1] :
							j += 1
						while j<k and arr[k] == arr[k-1] :
							k -= 1
						j += 1
						k -= 1
		return result
arr = [0,0,0,0]
print threesum(arr)
