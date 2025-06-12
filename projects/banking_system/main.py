from datetime import datetime
import pytz
import time

class BankAccount:
    bank_name = "PNB"
    bank_branch = "Noida"
    bank_currency = 'Rs.'
    total_accounts = 0
    next_account_number = 1001

    def __init__(self, name, balance, acc_type='Savings'):
        if BankAccount.is_valid_minimum_balance(balance):
            raise ValueError("The initial balance should not be less than Rs. 1000")
        
        self.acc_number = BankAccount.next_account_number
        self.name = name
        self.balance = balance
        self.acc_type = acc_type
        self.acc_creation = time.time()
        self.timezone = pytz.timezone('Asia/Kolkata')
        self.last_transaction_id = 1
        self.transactions = {
            self.last_transaction_id:{
                'message': f'Account created',
                'action': self.balance,
                'curr_balance': self.balance,
                'date-time': self.acc_creation,
                'status': 'Successful',
                'verbose': f'Account Created with a balance of {self.bank_currency} {self.balance}.'
                }
            }
        BankAccount.total_accounts+=1
        BankAccount.next_account_number+=1

    def deposit(self, amount):
        self.balance+=amount
        self.last_transaction_id+=1
        self.transactions[self.last_transaction_id] = {
                    'message': f'Account Credited',
                    'action': amount,
                    'curr_balance': self.balance,
                    'date-time': time.time(),
                    'status': 'Successful',
                    'verbose': ''
                }
    

    def withdraw(self, amount):
        if amount > self.balance:
            self.last_transaction_id+=1
            self.transactions[self.last_transaction_id] = {
                        'message': f'Insufficient Balance',
                        'action': 0,
                        'curr_balance': self.balance,
                        'date-time': time.time(),
                        'status': 'Failed',
                        'verbose': f'Account debit failed, tried to debit {self.bank_currency} {amount}.'
                    }
        else:
            self.balance-=amount
            self.last_transaction_id+=1
            self.transactions[self.last_transaction_id] = {
                        'message': f'Account Debited',
                        'action': -amount,
                        'curr_balance': self.balance,
                        'date-time': time.time(),
                        'status': 'Successful',
                        'verbose': ''
                    }

    def details(self):
        print(f"Name: {self.name}\nAcc id: {self.acc_number}\nAcc type: {self.acc_type}\nCreated on: {self.display_time(self.acc_creation, self.timezone)}\nBalance: {self.bank_currency} {self.balance}\nRecent Transaction: {self.transactions[self.last_transaction_id]['message']}\n")

    def view_transaction_history(self, verbose=False):
        for transaction_id in self.transactions:
            transaction = self.transactions[transaction_id]
            print(f"Transaction ID: {transaction_id}\n-------------------\nMessage: {transaction['message']}")
            print(f"{'Credit' if transaction['action'] >=0 else 'Debit'} amount: {self.bank_currency} {abs(transaction['action'])}")
            print(f"Balance: {self.bank_currency} {transaction['curr_balance']}")
            print(f"Status: {transaction['status']}")
            print(f"{self.display_time(transaction['date-time'], self.timezone)}")
            if verbose:
                print(f"Verbose: {transaction['verbose']}")
            print()

    @classmethod
    def show_total_accounts(cls):
        print(f'Total number of accounts: {BankAccount.total_accounts}\n')
    
    @classmethod
    def show_bank_details(cls):
        print(f"Bank name: {BankAccount.bank_name}\nBank branch: {BankAccount.bank_branch}\n")

    @staticmethod
    def is_valid_minimum_balance(amount):
        if amount < 1000:
            return False
        
    @staticmethod
    def display_time(epoch, timezone):
        return datetime.fromtimestamp(epoch, timezone).strftime("%d %B %Y, %I:%M %p")


acc1 = BankAccount('Rahul', 10000)
acc1.details()
acc1.withdraw(2000)
acc1.deposit(3000)
acc1.withdraw(15000)
acc1.withdraw(1000)
acc1.details()

acc1.view_transaction_history()

# acc2 = BankAccount('Ansh', 10000)
# acc2.details()
# acc3 = BankAccount('Ram', 10000)
# acc3.details()

# BankAccount.show_total_accounts()

# BankAccount.show_bank_details()