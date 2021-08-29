import math


class Solution:
    def reverse(self, x: int) -> int:
        x  = str(x)
        sign = x[0]
        int_array = [s for s in x]
        if sign == '-':
            int_array = int_array[1:]
        int_array.reverse()
        ans =  "".join(int_array)
        if sign == '-':
            ans =  "-" + ans
        ans = int(ans)
        if ans < -math.pow(2,31) or ans>math.pow(2,31)-1:
            return 0
        return int(ans)
if __name__ == '__main__':
    sol=Solution()
    print(sol.reverse(-321))
    print(sol.reverse(1534236469))
