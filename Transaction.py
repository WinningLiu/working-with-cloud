class Transaction:
    def __init__(self, id, amount, transaction, associatedAcc):
        self.id = id
        self.amount = amount
        self.transaction = transaction
        self.associatedAcc = associatedAcc
    def setId(self, id):
        self.id = id
    def setAmount(self, amount):
        self.amount = amount
    def setTransaction(self, transaction):
        self.transaction = transaction
    def setAssociatedAcc(self, associatedAcc):
        self.associatedAcc = associatedAcc