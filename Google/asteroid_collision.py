class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        def collison():
            stone1 = stack.pop()
            stone2 = stack.pop()
            if stone2>abs(stone1):
                stack.append(stone2)
            elif stone2<abs(stone1):
                stack.append(stone1)

        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                collison()

        return stack



if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([5,10,-5]))
    # print(sol.asteroidCollision([8,-8]))
    # print(sol.asteroidCollision([10,2,-5]))
    # print(sol.asteroidCollision([-2,-1,1,2]))
