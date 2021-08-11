class Solution:
    def __init__(self):
        self.ans = []
    def subsets(self, nums):
        def get_subsets(input, output):
            if len(input) == 0:
                print("output", output)

                self.ans.append(output[:])
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
    sol.subsets([1,2,3])
    print("sol", sol.ans)



