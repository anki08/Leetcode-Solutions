from collections import defaultdict
class Solution:
    def findReplaceString(self, s: str, indices, sources, targets):
        new_str = []
        start = 0
        dict = defaultdict(list)
        for i in range(len(indices)):
            dict[indices[i]].append(sources[i])
            dict[indices[i]].append(targets[i])

        indices = sorted(indices)
        for i in range(len(indices)):
            new_str.append(s[start:indices[i]])
            new_str.append(s[indices[i]:indices[i]+len(dict[indices[i]][0])])
            start = indices[i]  + len(sources[i])+1
        new_str.append(s[start:])
        print (new_str)

        for i in range(len(indices)):
            for j in range(len(new_str)):
                if dict[indices[i]][0] == new_str[j]:
                    new_str[j] = dict[indices[i]][1]
        print("new", new_str)
        return "".join(new_str[i] for i in range(len(new_str))if len(new_str[i]) > 0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]))
    print(sol.findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
    print(sol.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))
    print(sol.findReplaceString("wqzzcbnwxc", [5,2,7], ["bn","zzc","wxc"], ["t","lwb","nee"]))