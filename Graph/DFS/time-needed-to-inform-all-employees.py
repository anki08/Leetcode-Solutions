import collections
global res
res = 0
def numOfMinutes(n: int, headID: int, manager, informTime) -> int:
    # res = 0
    def dfs(manager, time):
        global res
        res = max(res, time)
        for subordinate in subordinates[manager]:
            dfs(subordinate, time+informTime[manager])


    subordinates = collections.defaultdict(list)
    for i , v in enumerate(manager):
        subordinates[v].append(i)
    print(subordinates)


    dfs(headID, 0)
    return res

if __name__ == '__main__':
    print(numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))
    # print(numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
    # print(numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))