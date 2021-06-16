def letterCombinations(digits: str):
    if(len(digits) == 0):
        return  0


    num_map = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    res = []


    def backtrack(index, substring):
        if(len(substring) == len(digits)):
            res.append("".join(substring))
            return res

        possible_characters = num_map[digits[index]]
        for i in range(len(possible_characters)):
            substring.append(possible_characters[i])
            backtrack(index+1, substring)
            substring.pop()

    backtrack(0,[])
    return res



if __name__ == '__main__':
    digits = "23"
    print(letterCombinations(digits))