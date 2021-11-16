import numpy as np
class Solution2:
    def maxScore(self, cardPoints, k):
        def util(k, lindex, rindex):
            if k==0:
                return 0
            return max(cardPoints[rindex]+util(k-1, lindex, rindex-1), cardPoints[lindex]+util(k-1, lindex+1, rindex))
        return util(k, 0, len(cardPoints)-1)

class Solution:
    def maxScore(self, cardPoints, k):
        dp_front = np.full((k+1), 0)
        dp_rear = np.full((k+1), 0)
        for i in range(k):
                dp_front[i] = cardPoints[i]
                dp_rear[i] = cardPoints[len(cardPoints)-i-1]
        l, r= 0, 0
        sum_w = 0
        while k>0:
            if dp_front[l]<dp_rear[r]:
                sum_w += dp_rear[r]
                r+=1
            elif dp_front[l]>dp_rear[r]:
                sum_w += dp_front[l]
                l+=1
            elif dp_front[l]==dp_rear[r]:
                sum_w += dp_front[l]
                l+=1
                r+=1
            k -=1


        print(sum_w)
if __name__ == '__main__':
    sol = Solution()
    # print(sol.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
    print(sol.maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3))