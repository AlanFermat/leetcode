def mergeInterval(intervalList, targetInterval):
	
	if not intervalList:
		return -1
	intervalList = sorted(intervalList)
	if intervalList[0][0] > targetInterval[0]:
		return -1
	print (intervalList)
	n = len(intervalList)
	dp = [[0,[]] for _ in range(n)]
	print (dp)
	# dp[i] if we include interval i then how many steps we need to 
	# get the coverage of the targetInterval
	


	print (dp)










intervalList = [[-1,9],[1,10],[0,3],[9,10],[3,14],[2,9],[10,16]]
targetInterval = [2, 15]
mergeInterval(intervalList, targetInterval)