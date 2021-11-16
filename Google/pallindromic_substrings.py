class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.sub(s, i, i)
            ans += self.sub(s, i, i+1)
        return ans

    def sub(self,s, low, high):
        count = 0
        while s[low] == s[high]:
            low-=1
            high+=1
            count+=1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("abc"))