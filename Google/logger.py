class Logger:

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hashmap and timestamp - self.hashmap[message]  < 10:
            # self.hashmap[message] = timestamp
            return False
        elif message not in self.hashmap or timestamp - self.hashmap[message]  >= 10:
            self.hashmap[message] = timestamp
            return True


if __name__ == '__main__':
    log = Logger()
    print(log.shouldPrintMessage(1, "foo"))
    print(log.shouldPrintMessage(2, "bar"))
    print(log.shouldPrintMessage(3, "foo"))
    print(log.shouldPrintMessage(8, "bar"))
    print(log.shouldPrintMessage(10, "foo"))
    print(log.shouldPrintMessage(11, "foo"))