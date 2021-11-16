class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations = sorted(citations, reverse=True)
        count = 0
        while count < n and citations[n-count-1] > count:count+=1
        return count




if __name__ == '__main__':
    sol = Solution()
    # print("ans:", sol.hIndex([3, 0, 6, 1, 5]))
    print("ans:",sol.hIndex([1,3,1]))
    # print("ans:", sol.hIndex([100]))
