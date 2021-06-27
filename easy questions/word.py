def longestWord(words) -> str:
    words = sorted(words)
    print(words)
    words = sorted(words, key=lambda x: len(x), reverse=True)
    print(words)
    for word in words:
        if all(word[:k] in words for k in range(1, len(word))):
            return word
    return ""


if __name__ == '__main__':
    words = ["k", "lg", "it", "oidd", "oid", "oiddm", "kfk", "y", "mw", "kf", "l", "o", "mwaqz", "oi", "ych", "m",
             "mwa"]
    print(longestWord(words))
