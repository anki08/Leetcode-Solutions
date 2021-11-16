import heapq
import numpy
import numpy as np
from collections import defaultdict, OrderedDict

class Solution:
    def __init__(self):
        self.disqualifiedCharacters = [[0] * 26 for i in range(6)]

    def findSecretWord(self, wordlist, master: 'Master') -> int:
        f = np.zeros((26, 6), dtype=int)
        for i in range(len(wordlist)):
            for j, ch in enumerate(wordlist[i]):
                f[ord(ch)-ord('a')][j] += 1

        score = defaultdict(list)
        for i in range(len(wordlist)):
            s = 0
            for j, ch in enumerate(wordlist[i]):
                s += f[ord(ch)-ord('a')][j]
            score[s].append(wordlist[i])

        s = sorted(score.items(), key = lambda i: i[0], reverse=True)
        score = OrderedDict(s)

        print(score)
        x = 0
        while x < 6:
            for key, val in score.items():
                for j , word in enumerate(val):
                    x = master.guess(word)
                    if x == 0:
                        for k, letter in enumerate(word):
                            self.disqualifiedCharacters[k][ord(letter) - ord('a')] = 1
                    if x == 6:
                        print("found")
                        return True


    def no_of_word_match(self, word1, word2):
        ch= 0
        count = 0
        while ch<len(word1) and ch<len(word2):
            if word1[ch] == word2[ch]:
                count += 1
            ch += 1
        return count

    def isNotDisqualified(self, a: str) -> bool:
        for j, letter in enumerate(a):
            if self.disqualifiedCharacters[j][ord(letter) - ord('a')] == 1:
                return False
        return True

class Master:
    def __init__(self, word):
        self.given_word = word

    def guess(self, word2):
        sol = Solution()
        return sol.no_of_word_match(self.given_word, word2)

if __name__ == '__main__':
    sol  = Solution()
    m = Master("hbaczn")
    print(sol.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], m))