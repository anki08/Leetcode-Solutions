def isPalindrome(s: str) -> bool:
    s = ''.join(x for x in s if x.isalpha())
    s = s.lower()
    return is_pallin(s)


def is_pallin(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s = "madam"
    print(isPalindrome(s))