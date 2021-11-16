from collections import Counter, defaultdict
class Solution:
    def isNStraightHand(self, hand, groupSize):
        count = Counter(hand)
        keys = sorted(count.keys())
        k = 0
        while k < len(keys):
            key_next = keys[k]
            if count[key_next]>0:
                for i in range(groupSize):
                    if count[key_next] ==0:
                        return False
                    count[key_next]-=1
                    key_next = key_next+1
            if count[keys[k]] == 0:
                k+=1
        return True


if __name__ == '__main__':
    sol  = Solution()
    # print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
    # print(sol.isNStraightHand(hand = [1,2,3,4,5,6], groupSize = 2))
    # print(sol.isNStraightHand(hand = [2,1], groupSize = 2))
    print(sol.isNStraightHand(hand = [1,1,2,2,3,3], groupSize = 3))