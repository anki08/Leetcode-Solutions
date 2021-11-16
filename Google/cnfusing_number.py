class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotate180 = [[0, 0], [1, 1], [6, 9], [8, 8], [9, 6]]
        res = 0

        def util(num, rotated_num, unit):
            nonlocal res
            if num != rotated_num:
                res += 1

            for d, dRotated in rotate180:
                if d == 0 and num == 0: continue
                if num * unit + d > n: break
                util(num * unit + d, dRotated * unit + rotated_num, unit * 10)

        util(0, 0, 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.confusingNumberII(20))
