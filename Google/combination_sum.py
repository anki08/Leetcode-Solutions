class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def util(start, end, target, output):
            if target == 0:
                ans.append(output[:])
            elif(target>0):
                for i in range(start, end):
                    output.append(candidates[i])
                    util(i, end, target-candidates[i], output)
                    output.pop()
        util(0, len(candidates), target, [])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum(candidates = [2,3,6,7], target = 7))