class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []
        map = {
            "2" : "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        ans = []
        def backtrack(output, index):
            if len(digits) == index:
                ans.append("".join(output))
                return
            letters = map[digits[index]]
            for ch in letters:
                output.append(ch)
                backtrack(output, index+1)
                output.pop()
        backtrack([], 0)
        return (ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))