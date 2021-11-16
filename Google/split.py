from collections import Counter
class Solution:
    def isPossible(self, nums):
        count = Counter(nums)
        for val in count.keys():
            a = val
            grp_size = 0
            if count[a] != 0:
                while True:
                    if a not in count or count[a]==0:
                        if grp_size <3:
                            return False
                        break
                    elif count[a]>0:
                        count[a] -=1
                        grp_size += 1

                    if grp_size == 3:
                        break
                    a = a+1
        return True


if __name__ == '__main__':
    sol = Solution()
    # print(sol.isPossible([1,2,3,3,4,5]))
    print(sol.isPossible([1,2,3,3,4,4,5,5]))