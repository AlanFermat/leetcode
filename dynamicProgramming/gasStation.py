"""
A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

"""
def minRefuelStops(target, startFuel, stations):
    """
    :type target: int
    :type startFuel: int
    :type stations: List[List[int]]
    :rtype: int
    """
    if target <= startFuel:
        return 0
    n = len(stations)
    dp  = [startFuel] + [0 for _ in range(n)] 
    for i, (loc, fuel) in enumerate(stations):
        for j in range(i, -1, -1):
            if dp[j] >= loc:
                dp[j+1] = max(dp[j] + fuel, dp[j+1])
    
    for step, val in enumerate(dp):
        if val >= target:
            return step
    return -1