# res = []
def sort(stack):
    # nonlocal res
    if len(stack) == 0:
        return
    temp = stack.pop()
    sort(stack)
    # res = stack
    insert(stack, temp)
    print(stack)

def insert(stack, temp):
    if len(stack) == 0 or stack[-1] >=temp:
        stack.append(temp)
        return
    val = stack.pop()
    insert(stack, temp)
    stack.append(val)

sort([34,43,4354,54,35,434,34])
# print(res[::-1])