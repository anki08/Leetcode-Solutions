class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(1,len(strs)):
            string1 = string2 = 0
            while  string2<len(prefix) and string1<len(strs[i]) and strs[i][string1] == prefix[string2]:
                string1 += 1
                string2 += 1
            prefix = prefix[:string1]
        return prefix
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))


