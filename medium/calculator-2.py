from collections import defaultdict
def calculate(s):
    stack =  []
    s = s.replace(" ", "")
    operation = '+'
    number = ''
    for i, char in enumerate(s):
        if char.isdigit():
             number += char
        if not char.isdigit() or i == len(s)-1:
            if operation == '+':
                stack.append(int(number))
            elif operation == '-':
                stack.append(-int(number))
            elif operation == '*':
                stack.append(int(int(stack.pop())  * int(number)))
            elif operation == '/':
                stack.append(int(int(stack.pop())  / int(number)))
            operation = char
            number = ''

    result = 0
    while ( len(stack)> 0):
        result += stack.pop()
    print(result)
    return result

if __name__ == '__main__':
    s = "5*2/2-10"
    calculate(s)
