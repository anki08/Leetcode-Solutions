def maximumUnits(boxTypes, truckSize: int) -> int:
    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    number_of_boxes = 0
    total_units = 0
    for i in range(len(boxTypes)):
        for j in range(boxTypes[i][0]):
            if (number_of_boxes < truckSize):
                number_of_boxes += 1
                total_units += boxTypes[i][1]

    return total_units


if __name__ == '__main__':
    print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))