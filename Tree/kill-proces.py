from collections import defaultdict
import numpy as np
class Solution:
    def killProcess(self, pid, ppid, a):
        ans = []
        max_el = np.max(pid)
        parent = {x:x for x in range(max_el+1)}
        def find(node):
            if parent[node] == node:
                return parent[node]
            return find(parent[node])

        for i in range(len(pid)):
            if (pid[i] == a): continue
            x = find(pid[i])
            y = find(ppid[i])
            if x != y:
                parent[x] = y
        for x in pid:
            if x == a or find(x) == a:
                ans.append(x)
        return (ans)




if __name__ == '__main__':
    sol = Solution()
    sol.killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], a = 5)