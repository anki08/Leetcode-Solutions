class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if (key in self.hash):
            self.hash[key].append([timestamp, value])
        else:
            self.hash[key] = [[timestamp, value]]
        return None

    def get(self, key: str, timestamp: int) -> str:
        found = False
        if key in self.hash:
            val_list = self.hash[key]
            for i in range(len(val_list)):
                if (timestamp >= val_list[i][0] and (i == len(val_list) - 1 or timestamp < val_list[i + 1][0])):
                    found = True
                    return val_list[i][1]
        if(found == False):
            return "null"


if __name__ == '__main__':
    obj = TimeMap()
    obj.set("love","high",10)
    obj.set("love", "low", 20)
    param_2 = obj.get("love", 5)
    # param_3 = obj.get("love", 10)
    # param_4 = obj.get("love", 15)
    # param_5 = obj.get("love", 20)
    # param_6 = obj.get("love", 25)
    # print(param_2)
    # print(param_3)
    # print(param_4)
    # print(param_6)
    # print(param_5)


