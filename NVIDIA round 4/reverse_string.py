class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start<=end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        print(s)

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))