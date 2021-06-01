hashmap = {}
s = "anagram"
t = "nagaram"


def isAnagram(s: str, t: str) -> bool:
    hashmap = {}
    for i in s:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in t:
        if i in hashmap:
            hashmap[i] -= 1
        else:
            return False

    for key, value in hashmap.items():
        if (value > 0):
            return False

    return True

if __name__ == '__main__':
    print(isAnagram(s,t))