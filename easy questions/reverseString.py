def reverseString(arr):
    def helper(s_0, s_n, r):
        if (s_0 >= s_n):
            return
        r[s_0], r[s_n] = r[s_n], r[s_0]
        helper(s_0 + 1, s_n - 1, r)

    helper(0, len(arr) - 1, arr)
    print(arr)


if __name__ == '__main__':
    reverseString(["h", "e", "l", "l", "o"])
