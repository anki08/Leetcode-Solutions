from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs):
        master_map = defaultdict()
        res = []
        for word in strs:
            word_sorted = sorted(word)
            word_sorted = ''.join(word_sorted)
            if word_sorted in master_map:
                master_map[word_sorted].append(word)
            else:
                master_map[word_sorted] = [word]
        for key, val in master_map.items():
            res.append(val)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
