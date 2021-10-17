class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.d:
            self.d[message] = timestamp + 10
            return True
        else:
            if self.d[message] > timestamp:
                return False
            else:
                self.d[message] = timestamp + 10
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)