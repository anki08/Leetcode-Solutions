def generateParenthesis(n):
    res = []

    def backtrack(left=0, right=0, s=[]):
        if(len(s)==2*n):
            res.append("".join(s))
            return
        if(left < n):
            s.append('(')
            backtrack(left+1, right, s)
            s.pop()
        if(right < left):
            s.append(')')
            backtrack(left, right+1)
            s.pop()

    backtrack()
    return res

if __name__ == '__main__':
    print(generateParenthesis(3))
