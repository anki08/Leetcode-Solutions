def minRemoveToMakeValid(s):
    indexes_to_remove = set()
    open_brackets_stack = []
    ans = ""
    for i, char in enumerate(s):
        if char not in "()":
            continue
        if(char == "("):
            open_brackets_stack.append(i)
        elif(len(open_brackets_stack) == 0):
            indexes_to_remove.add(i)
        else:
            open_brackets_stack.pop()
    indexes_to_remove = indexes_to_remove.union(set(open_brackets_stack))
    for i,c in enumerate(s):
        if(i not in indexes_to_remove):
            ans += c
    return ans

if __name__ == '__main__':
    print(minRemoveToMakeValid(s = "lee(t(c)o)de)"))
    print(minRemoveToMakeValid(s = "a)b(c)d"))
    print(minRemoveToMakeValid(s = "))(("))
    print(minRemoveToMakeValid(s = "(a(b(c)d)"))