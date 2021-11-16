class Solution:
    def compress(self, chars):
        i = 0
        while i<len(chars):
            count = 1
            start = i
            flag = False
            while i<len(chars) and chars[i] == chars[i-1]:
                count+=1
                i+=1
                flag = True
            if flag == False:
                i+=1
            if count>1:
                chars[start] = count
        print(chars)
        print(start)



if __name__ == '__main__':
    sol = Solution()
    # print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(sol.compress(["a","a","a","b","b","a","a"]))
    # print(sol.compress(["a","a","b","b","c","c","c"]))
