
import numpy as np

def climb_stairs(n):
    arr = np.zeros(n+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]

if __name__ == '__main__':
    print(climb_stairs(6))