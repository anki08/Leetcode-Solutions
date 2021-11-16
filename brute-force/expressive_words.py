from collections import Counter

class Solution:
    def expressiveWords(self, s, words):
        count = 0
        for word in words:
            if self.isStretchy(s, word):
                count += 1
            else:
                print(word)
        return count

    def isStretchy(self, s, word):
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                s_letter_count = self.getDuplicateLength(s, i)
                word_letter_count = self.getDuplicateLength(word, j)

                if (s_letter_count < 3 and s_letter_count != word_letter_count) or (
                        s_letter_count >= 3 and word_letter_count > s_letter_count):
                    return False
            else:
                return False

            i += s_letter_count
            j += word_letter_count

        return i == len(s) and j == len(word)

    def getDuplicateLength(self, s, i):
        target = s[i]
        count = 0
        while i < len(s):
            if s[i] == target:
                count += 1
            else:
                break
            i += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.expressiveWords(s = "heeellooo", words = ["hello", "hi", "helo"]))