import numpy as np
def mctFromLeafValues(arr) -> int:
    arr = np.array(arr)

    def mctFromLeafValuesUtil(arr, i, j):
        if(i>j):
            return 0
        if (j - i == 1):
            print("base", i,j)
            return arr[j] * arr[i]

        min_val =100000000

        for k in range(i,j):
            print("i ", i, "k ", k, "j ", j)
            print("1 ", arr[i:k], arr[k+1:j+1])
            print("2 ", np.max(arr[i:k+1]) , np.max(arr[k+1:j+1]))
            print("2 ", np.max(arr[i:k+1]) * np.max(arr[k+1:j+1]))
            val1 = mctFromLeafValuesUtil(arr, i, k)
            val2 = mctFromLeafValuesUtil(arr, k+1, j)
            print("CEEC",val1, val2)
            min_val = min(min_val, mctFromLeafValuesUtil(arr, i, k) + mctFromLeafValuesUtil(arr, k+1, j) + max(arr[i:k+1]) * max(arr[k+1:j+1]))
            # print("3 temp", temp)
            # min_val = min(min_val, temp)
        return min_val
    return mctFromLeafValuesUtil(arr, 0, len(arr)-1)

if __name__ == '__main__':
    print(mctFromLeafValues([6,2,4]))