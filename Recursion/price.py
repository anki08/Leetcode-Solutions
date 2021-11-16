class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        val = -1
        stack = []
        for i in range(len(prices)-1, -1, -1):
            while stack and prices[i]<stack[-1]:
                stack.pop()
            if stack:
                val = prices[i] - stack[-1]
            else:
                val = prices[i]
            stack.append(prices[i])
            prices[i] = val

        return prices



if __name__ == '__main__':
    sol = Solution()
    print(sol.finalPrices([8,4,6,2,3]))
    print(sol.finalPrices([1,2,3,4,5]))
    print(sol.finalPrices([10,1,1,6]))