from collections import deque
dict = {0:[1,2], 1:[3,4], 2:[5,6], 3:[7,8], 4:[9,10], 5:[11,12],6:[13,14]}
queue = deque()
queue.append(0)
step = 0
while queue:
    step += 1
    id = queue.pop()
    for child in dict[id]:
        print(f'step {step} , {queue}')
        queue.append(child)