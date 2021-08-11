from collections import  defaultdict
class Solution:
    def __init__(self):
        self.ans = []
    def subsets(self, nums):
        def get_subsets(input, output):
            if len(input) == 0:
                res = output[:]
                print("output", res)
                if sorted(res) not in self.ans:
                    self.ans.append(sorted(res))
                return
            output.append(input[0])
            input = input[1:]
            get_subsets(input, output)
            output.pop()
            get_subsets(input, output)
            return

        get_subsets(nums, [])


if __name__ == '__main__':
    sol = Solution()
    sol.subsets([4,4,4,1,4])
    print("sol", sol.ans)



