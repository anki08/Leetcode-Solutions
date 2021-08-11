def tower_of_hanoi(no_of_disks, source, destination, helper):
    if no_of_disks == 1:
        print ("move disk from {0} to {1}".format(source, destination))
        return

    tower_of_hanoi(no_of_disks-1, source, helper, destination)
    print("move disk from {0} to {1}".format(source, destination))
    tower_of_hanoi(no_of_disks-1, helper, destination, source)




n = 4
tower_of_hanoi(n, 'A', 'C', 'B')
