class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.logger:
            if ((timestamp - self.logger[message] - timestamp) >= 10):
                self.logger[message] = timestamp
                return True
            else:
                return False
        else:
            self.logger[message] = timestamp
            return True


log = Logger()
arr = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
for i in range(len(arr)):
    log.shouldPrintMessage(arr[i][0], arr[i][1])
