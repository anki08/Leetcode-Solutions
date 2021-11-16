from collections import Counter
class Solution:
    def isPossibleDivide(self, nums, k):
        count = Counter(nums)
        keys = sorted(count.keys())
        i = 0
        while i<len(keys):
            a = keys[i]
            grp_size = 0
            if count[a] != 0:
                while True:
                    if a not in count or count[a] == 0:
                        if grp_size < k:
                            return False
                        break
                    elif count[a] > 0:
                        count[a] -= 1
                        grp_size += 1

                    if grp_size == k:
                        break
                    a = a + 1
            if count[keys[i]] == 0:
                i += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
    print(sol.isPossibleDivide( nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    print(sol.isPossibleDivide( nums = [3,3,2,2,1,1], k = 3))
    print(sol.isPossibleDivide(nums = [1,2,3,4], k = 3))
    print(sol.isPossibleDivide([1,2,3,4,5,1,2,3,4,5,1,2,3,4], 5))