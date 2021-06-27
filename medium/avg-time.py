def avg_time(checkin, checkout):
    sum = 0
    count = 0
    for i in checkin:
        for j in checkout:
            if (i[0] == j[0]):
                sum += j[1] - i[1]
                count += 1
                print("here", sum)
                print("here", count)
                break
    ans = (sum / count)
    return ans


if __name__ == '__main__':
    checkin = [[45, 3], [27, 10], [10, 24]]
    checkout = [[2, 3], [45, 15], [27, 20]]
    print(avg_time(checkin, checkout))
