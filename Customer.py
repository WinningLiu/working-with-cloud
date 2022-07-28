class Customer:
    def __init__(self, id, firstName, lastName, associatedAcc):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.associatedAcc = associatedAcc
    def setId(self, id):
        self.id = id
    def setFirstName(self, firstName):
        self.firstName = firstName
    def setLastName(self, lastName):
        self.lastName = lastName
    def setAssociatedAcc(self, associatedAcc):
        self.associatedAcc = associatedAcc