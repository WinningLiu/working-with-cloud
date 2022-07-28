from flask import Flask, redirect, url_for, request

app = Flask(__name__)

from Account import Account
from Customer import Customer
from Transaction import Transaction

import json

accounts = {}
customers = {}
transactions = {}

@app.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        data = json.loads(request.data)
        account1 = Account(data["id"], data["accNum"], data["balance"], data["accStatus"])
        accounts[data["id"]] = account1
        return [data["id"], data["accNum"], data["balance"], data["accStatus"]]

    else:
        return accounts[data["id"]]

# @app.route('/customer')
# def customer():
#     accounts = {}

#     account1 = Account(1, "02103i", 0.00, "Open")
#     accounts[1] = account1

#     print(accounts[1].accNum)
#     return "Account ", 1, " added."

# @app.route('/transaction')
# def transaction():
#     accounts = {}

#     account1 = Account(1, "02103i", 0.00, "Open")
#     accounts[1] = account1

#     print(accounts[1].accNum)
#     return "Account ", 1, " added."

if __name__ == "__main__":
    app.run(debug=True)