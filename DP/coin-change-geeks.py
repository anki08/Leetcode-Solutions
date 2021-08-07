import numpy as np
def count(S, m, amount):
    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = np.zeros((amount+1,m), dtype=int)

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, amount + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = max(x , y)
    print(table)

    return table[amount][m - 1]


# Driver program to test above function
arr = [1, 2, 5]
m = len(arr)
amount = 11
print(count(arr, m, amount))