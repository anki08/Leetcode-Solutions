class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans

if __name__ == '__main__':
    sol = Solution()
    # print(sol.asteroidCollision([5,10,-5]))
    # print(sol.asteroidCollision([8,-8]))
    # print(sol.asteroidCollision([10,2,-5]))
    print(sol.asteroidCollision([-2,-1,1,2]))