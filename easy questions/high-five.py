def highFive(items):
    result = {}
    items = sorted(items, key=lambda x: x[1], reverse=True)
    for i in items:
        if (i[0] in result and result[i[0]][1] < 4):
            result[i[0]][0] += i[1]
            result[i[0]][1] += 1
        elif (i[0] not in result):
            result[i[0]] = [i[1], 0]

    result_list = []
    for key, value in result.items():
        stud = []
        stud.append(key)
        stud.append(int(value[0] / 5))
        result_list.append(stud)
    # print(result)
    return result_list


if __name__ == '__main__':
    print(
        highFive([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
