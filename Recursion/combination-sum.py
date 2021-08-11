class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum(self, candidates, target: int):

        def combination_sum_util(target, candidates, output, start, end):
            if target == 0:
                self.ans.append(output[:])
                return
            elif (target > 0):
                for i in range(start, end):
                    output.append(candidates[i])
                    combination_sum_util(target - candidates[i], candidates, output, i, end)
                    output.pop()

        combination_sum_util(target, candidates, [], 0, len(candidates))


if __name__ == '__main__':
    sol = Solution()
    sol.combinationSum([2, 3, 6, 7], 7)
    print(sol.ans)
