def reverse_bits(n):
    bits = f'{6:032b}'
    print(bits)
    bits  = bits[::-1]
    return bits


if __name__ == '__main__':
    print(reverse_bits(1))
