def plusOne(digits):
    sum = 0
    carry = 0
    digits.reverse()
    for i in range(len(digits)):
        sum = digits[i] + 1
        carry = int(sum / 10)
        sum = sum % 10
        digits[i] = sum
        if carry == 0:
            break
    if carry == 1:
        digits.append(1)
    digits.reverse()

    return digits


if __name__ == '__main__':
    dig = [9, 9]
    print(plusOne(dig))
