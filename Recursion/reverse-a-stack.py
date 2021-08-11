class Sol:
    def __init__(self):
        self.ans = []
    def reverse(self, stack):
        if len(stack) == 0:
            return
        temp = stack.pop()
        self.ans.append(temp)
        self.reverse(stack)
        stack.append(temp)

if __name__ == '__main__':
    s = Sol()
    s.reverse([1,2,3,4,5,6])
    print(s.ans)
