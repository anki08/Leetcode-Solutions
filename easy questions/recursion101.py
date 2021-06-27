def reverse(s):
    if (len(s) == 0):
        return

    reverse(s[1:])
    print(s[0])


if __name__ == '__main__':
    reverse("abcdefgh")
