class Solution:
    def min_absolute_sum(self, nums1):
        target = sum(nums1)
        def util(index, sum_calc):
            if index==0:
                return abs((target-sum_calc)-sum_calc)
            return min(util(index-1, sum_calc-nums1[index]), util(index-1, sum_calc))
        return util(len(nums1)-1, target)

if __name__ == '__main__':
    sol = Solution()
    print(sol.min_absolute_sum([3, 1, 4, 2, 2, 1]))