class Solution:
    def generatePalindromes(self, s: str):
        ans = []

        def generate_util(input, output, start, end):
            if len(output) == len(input) and output == output[::-1]:
                ans.append("".join(output))
                return
            elif len(output) == len(input) :
                return
            for i in range(start, end):
                output.append(s[i])
                generate_util(input, output, start, end)
                output.pop()
        generate_util(s, [], 0, len(s))
        print(ans)



if __name__ == '__main__':
    sol = Solution()
    print(sol.generatePalindromes("aabb"))
