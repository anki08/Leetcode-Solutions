def slowestKey( releaseTimes, keysPressed):
    hashkey = {}
    for i in range(len(keysPressed)):
        if (keysPressed[i] in hashkey):
            val = releaseTimes[0] if i == 0 else releaseTimes[i] - releaseTimes[i - 1]
            if (val > hashkey[keysPressed[i]]):
                hashkey[keysPressed[i]] = val
        else:
            val = releaseTimes[0] if i == 0 else releaseTimes[i] - releaseTimes[i - 1]
            hashkey[keysPressed[i]] = val

    max_val = 0
    lexi_keys = sorted(hashkey,reverse=True)
    max_values = sorted(hashkey.values(),reverse=True)
    max_value = max_values[0]
    for i in lexi_keys:
        if(hashkey[i] == max_value):
            return i


if __name__ == '__main__':
    print(slowestKey([9,29,49,50], "cbcd"))
