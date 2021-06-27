import numpy as np


def fib(n: int) -> int:
    if n <= 1:
        return n
    if (n == 2):
        return 1
    arr = np.zeros(n + 1, int)
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


if __name__ == '__main__':
    print(fib(3))
