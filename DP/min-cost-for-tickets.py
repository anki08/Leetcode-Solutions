import numpy as np
def mincostTickets(days, costs) -> int:

    dp = np.full(days[-1]+1, 0, dtype=int)
    travel = np.full(days[-1]+1, False)
    for i in days:
        travel[i] = True
    for i in range(1, days[-1]+1):
        if travel[i] == False:
            dp[i] = dp[i-1]
            continue
        dp[i] = min(costs[0] + dp[max(i-1,0)], costs[1] + dp[max(i-7,0)], costs[2] + dp[max(i-30, 0)])
    return (dp[-1])



if __name__ == '__main__':
    mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])
    mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15])