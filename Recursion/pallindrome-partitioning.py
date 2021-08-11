class Solution:
    def __init__(self):
        self.ans = []
    def partition(self, s: str):

        def partition_util(s, start, end, output):
            if start == end:
                self.ans.append(output[:])

            for i in range(start, end):
                current = s[start:i+1]
                if current == current[::-1]:
                    output.append(current)
                    partition_util(s, i+1, end, output)
                    output.pop()

        partition_util(s, 0, len(s), [])

if __name__ == '__main__':
    sol = Solution()
    sol.partition("aab")
    print(sol.ans)

