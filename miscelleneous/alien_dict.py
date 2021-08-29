class Solution:
    def isAlienSorted(self, words, order):
        # order = [x for x in order]
        # order = list(set(order))
        # order = "".join(order)
        order  = " " + order
        if len(words) == 1:
            return True
        # sorted_words = sorted(words, key = lambda x:len(x))
        # if sorted_words != words:
        #     return False
        for i in range(1, len(words)):
            for ch in range(len(words[i-1])):
                if ch >= len(words[i]):
                    words[i] += " "
                if words[i][ch] == words[i-1][ch]:
                    continue
                if self.compare(words[i-1][ch], words[i][ch], order) == False:
                    return False
                else:
                    break
        return True



    def compare(self, word1, word2, order):
        index_word1 = order.find(word1)
        index_word2 = order.find(word2)
        if index_word1 > index_word2:
            return False
        return True



if __name__ == '__main__':
    sol  =Solution()
    print(sol.isAlienSorted(["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
    # print(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
    # print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))