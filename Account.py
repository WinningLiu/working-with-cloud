class Account:
    def __init__(self, id, accNum, balance, accStatus):
        self.id = id
        self.accNum = accNum
        self.balance = balance
        self.accStatus = accStatus
    def setId(self, id):
        self.id = id
    def setAccount(self, accNum):
        self.accNum = accNum
    def setBalance(self, balance):
        self.balance = balance
    def setStatus(self, accStatus):
        self.accStatus = accStatus