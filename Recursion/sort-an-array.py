temp = 0
def sort(arr):
    if len(arr) == 0:
        return
    temp = arr.pop()
    sort(arr)
    insert(arr, temp)
    print(arr)

def insert(arr, temp):
    if len(arr) == 0 or arr[-1]<= temp:
        arr.append(temp)
        return
    val = arr.pop()
    insert(arr, temp)
    arr.append(val)

sort([2,3,7,6,4,5, 9])
