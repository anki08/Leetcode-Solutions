import random


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.set = {}

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.list.append(val)
        self.set = set(self.list)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.list.pop(val)
        self.set = set(self.list)
        return True


    def getRandom(self) -> int:
        return random.sample(self.list, 1)


if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(2))
    print(obj.insert(3))
    print(obj.insert(4))
    print(obj.remove(2))
    print(obj.getRandom())