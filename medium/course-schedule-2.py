def findOrder(numCourses, prerequisites):
    sorted_pre = sorted(prerequisites, key=lambda x: x[1])
    pre = [x[1] for x in sorted_pre]
    pre = list(set(pre))
    if len(pre) < numCourses:
        cou = [x[0] for x in sorted_pre]
        cou = list(set(cou))
        pre.extend(cou)
    res = list(set(pre))
    if (len(res) < numCourses):
        res = [n for n in range(numCourses)]
    return res


if __name__ == '__main__':
    numCourses, prerequisites = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(findOrder(numCourses, prerequisites))
