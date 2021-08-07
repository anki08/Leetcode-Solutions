def print_f(n):
    if n == 0:
        return
    print_f(n-1)
    print (n)

if __name__ == '__main__':
    print_f(4)