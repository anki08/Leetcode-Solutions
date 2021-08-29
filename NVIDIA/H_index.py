class Solution:
    def hIndex(self, citations):
        n = len(citations)
        if n == 0: return 0
        for h in range(len(citations), -1, -1):
            # print(f"h : {h}")
            count_greater = 0
            count_smaller = 0
            for j in citations:
                if j < h:
                    count_smaller += 1
                elif j >= h:
                    count_greater += 1
            # print(f'smaller {count_smaller} greater {count_greater}')
            if count_greater >= h and count_smaller <= n - h:
                return h

        return 0


if __name__ == '__main__':
    sol = Solution()
    print("ans:", sol.hIndex([3, 0, 6, 1, 5]))
    print("ans:",sol.hIndex([1,3,1]))
    print("ans:", sol.hIndex([100]))
