def zeros_in_100_factorial(n):
    if n<0:
        return -1
    count = 0
    while n>1:
        n = n//5
        count += n
    return count

if __name__ == '__main__':
    print(zeros_in_100_factorial(5))
    print(zeros_in_100_factorial(10))
    print(zeros_in_100_factorial(25))