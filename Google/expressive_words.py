from collections import Counter
class Solution:
    def expressiveWords(self, s, words):
        s_a=[]
        [s_a.append(x) for x in s if x not in s_a]


        s_count = Counter(s)
        count = 0
        for word in words:
            w_count = Counter(word)
            non_dup_word = []
            [non_dup_word.append(x) for x in word if x not in non_dup_word]
            flag = True
            if non_dup_word!=s_a:
                flag=False
            for ch in non_dup_word:
                if ch not in s_count:
                    flag = False
                elif ch in s_count and w_count[ch]!=s_count[ch] and s_count[ch] < w_count[ch]+2:
                    flag = False

            if flag==True:
                count += 1

        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"]))
    print(sol.expressiveWords(s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]))
    print(sol.expressiveWords(s = "abcs", words = ["abc"]))
