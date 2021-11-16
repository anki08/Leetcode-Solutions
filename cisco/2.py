
def f(values):
    hashmap = {')':'(', '}':'{', ']':'['}
    s = []
    res = []
    flag = False
    for ex in values:
        flag = False
        for ch in ex:
            if ch in hashmap:
                if s:
                    t = s.pop()
                    if hashmap[ch] != t:
                        res.append('NO')
                        flag = True
                        break
                else:
                    res.append('NO')
                    flag = True
                    break
            elif ch in {'(' , '{', '['}:
                s.append(ch)
        if not s and flag == False:
            res.append("YES")
        s = []
    print(res)

if __name__ == '__main__':
    val = ['[{()()}({[]})]({}[({})})(((((((){})){}))[]{{{({({({{{{{{}}}}}})})})}}}))[][][]{']
    f(val)

