no = -132
sign = False
if (no < 0):
    no = abs(no)
    sign = True
rev = no % 10
no = int(no / 10)
while (no > 0):
    i = no % 10
    rev = rev * 10 + i
    no = int(no / 10)
if (sign):
    rev = -rev
if (rev > (2 ** 31) or rev <= -(2 ** 31)):
    rev = 0
print(rev)
