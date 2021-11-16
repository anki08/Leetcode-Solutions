class Solution:
    def findCelebrity(self, n: int) -> int:
        parent = {x:1 for x in range(n)}
        for i in range(n):
            for j in range(n):
                if knows(i,j)and !knows(j,i) and i!=j:
                    parent[j]+=1
        print(parent)
        max_val = max(list(parent.values()))
        count, ans= 0, 0
        for key, value in parent.items():
            if value == max_val:
                count +=1
                ans = key
        if max_val==n:
            return ans
        else:
            return -1
