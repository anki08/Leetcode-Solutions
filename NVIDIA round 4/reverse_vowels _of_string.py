class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s)-1
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        s = [x for x in s]
        while start<end:
            if s[start] not in vowels:
                start+=1
            if s[end] not in vowels:
                end-=1
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1
        print("".join(s))


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseVowels("hello"))