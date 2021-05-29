hash = [[1,1] , [1,2], [1,3], [2,1]]
key = 2
val = 2
seen = False
for i in range(len(hash)):
    if(key == hash[i][0]):
        hash[i] = [key, val]

        seen = True
if(seen == False):
    hash.append([key, val])
print(hash)
arr = []
for i in range(len(hash)):
    if(key != hash[i][0]):
        arr.append(hash[i])
hash = arr

print(hash)