class Solution:
    def partition(self, s: str):
        n = len(s)
        ans = []
        def partition_util(output, input, start, end):
            if start == end:
                ans.append(output[:])
            for i in range(start, end):
                current = s[start : i+1]
                if current == current[::-1]:
                    output.append(current)
                    partition_util(output, input, i+1, end)
                    output.pop()
        partition_util([], s, 0, len(s))
        return ans
if __name__ == '__main__':
    sol = Solution()
    print((sol.partition("aab")))