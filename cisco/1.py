def cost(x, y, a, b):
    return (abs(x - a) + abs(y - b))

def greedy(numpeople, x, y):
    xx, yy = [], []
    ans = 0
    for i in range(len(numpeople)):
        count = numpeople[i]
        while count > 0:
            xx.append(x[i])
            yy.append(y[i])
            count -=1

    xx = sorted(xx)
    yy = sorted(yy)

    mx = xx[len(xx) // 2]
    my = yy[len(yy) // 2]

    for i in range(len(numpeople)):
        ans += numpeople[i] * cost(mx, my, x[i], y[i])
    return ans

if __name__ == '__main__':
   nump = [1,2]
   x = [1,3]
   y = [1,3]
   print(greedy(nump, x, y))

   print(greedy([1,1], [1,3], [1,1]))