class Solution:
    def coinChange(self, coins, amount):
        def util(amount, index):
            if amount == 0:
                return 0
            if amount <0 and index>=0:
                return 9999999999
            if index ==-1 and amount>0:
                return 9999999999

            return min(util(amount, index-1), 1+util(amount-coins[index], index))

        ans = util(amount, len(coins)-1)
        if ans == 9999999999:
            return -1

        return util(amount, len(coins)-1)

if __name__ == '__main__':
    sol  = Solution()
    print(sol.coinChange(coins = [1,2,5], amount = 11))