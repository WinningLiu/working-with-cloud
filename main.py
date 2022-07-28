from Account import Account

def main():
    accounts = {}

    account1 = Account(1, "02103i", 0.00, "Open")
    accounts[1] = account1

    print(accounts[1].accNum)

if __name__ == "__main__":
    main()