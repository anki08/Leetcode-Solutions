class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.capacity = k
        self.start_index = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        self.queue[(self.start_index + self.count)% self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.start_index = (self.start_index + 1)% self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.start_index]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.start_index + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.capacity:
            return True
        return False

if __name__ == '__main__':
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())

