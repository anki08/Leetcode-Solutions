class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def util(input, output, target, start, end):
            if target == 0:
                ans.append(output[:])

            elif(target>0):
                for i in range(start, end):
                    output.append(input[i])
                    util(input, output,target-input[i], i+1, end)
                    output.pop()
        ans = []
        # candidates.sort(reverse=True)
        util(candidates, [], target, 0 , len(candidates))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([10,1,2,7,6,1,5], target = 8))
