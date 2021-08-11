def delete_mid(stack, k):
    if k==1:
        stack.pop()
        return
    temp = stack.pop()
    delete_mid(stack, k-1)
    stack.append(temp)
    print(stack)

delete_mid([1,2,3,4,5], 3)

