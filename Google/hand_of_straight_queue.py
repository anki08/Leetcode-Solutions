from collections import  Counter
class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize!=0:
            return False
        mp = Counter(hand)
        hands = sorted(hand)
        for val in hands:
            if mp[val]!=0:
                for gr in groupSize:
                    if mp[val+gr]==0:
                        return False
                    mp[val+gr] -=1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))