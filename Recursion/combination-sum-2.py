class Solution:
    def __init__(self):
        self.ans = []
    def combinationSum2(self, candidates, target):

        def combination_sum_util(candidates, output, target, start, end):
            if target  == 0:
                self.ans.append(output[:])
                return

            elif(target>0):
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    output.append(candidates[i])
                    combination_sum_util(candidates, output, target-candidates[i], i+1, end)
                    output.pop()

        combination_sum_util(candidates, [], target, 0, len(candidates))
if __name__ == '__main__':
    sol = Solution()
    sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(sol.ans)
