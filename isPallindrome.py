def validPalindrome(s: str) -> bool:
    isPallin = []
    if(isPallin.append(is_pallindrome(s, 0, len(s)-1))):
        return True
    low = 0
    high = len(s)-1
    while(low < high):
        if(s[low] == s[high]):
            low = low+1
            high = high-1
        else:
            if(is_pallindrome(s, low+1, high)):
                return True
            elif(is_pallindrome(s, low, high-1)):
                return True
            return False
    return True




def is_pallindrome(new_s, low, high):
    while(low < high):
        if (new_s[low] == new_s[high]):
            low = low + 1
            high = high - 1
        if (new_s[low] != new_s[high]):
            return False
    return True


if __name__ == '__main__':
    # s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"
    s = "aba"
    i = 0
    print(s[0:i])
    print(s[i+1:])
    # print(len(s))
    print(validPalindrome(s))
