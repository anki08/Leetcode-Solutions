class Solution:
    def subdomainVisits(self, cpdomains):
        hashmap = {}
        for dom in cpdomains:
            clicks = dom.split(" ")[0]
            sec = dom.split(" ")[1]
            arr = sec.split(".")
            # arr = arr[::-1]
            domains = []
            for i in range(len(arr)+1):
                op = ".".join(arr[i:])
                domains.append(op)
                if op not in hashmap and op != '':
                    hashmap[op] = int(clicks)
                elif op in hashmap and op != '':
                    hashmap[op] += int(clicks)

        print(hashmap)
        res = []
        for key, value in hashmap.items():
            res.append(str(value)+ " " + str(key))
        return res




if __name__ == '__main__':
    sol = Solution()
    print(sol.subdomainVisits(["9001 discuss.leetcode.com"]))
    print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))