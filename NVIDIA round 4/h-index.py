class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations = sorted(citations, reverse=True)
        i = 0
        while(i<citations[i]):
            i+=1
        return i




if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([3,0,6,1,5]))