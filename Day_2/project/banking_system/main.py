from datetime import datetime

class BankAccount:
    bank_name = "PNB"
    bank_branch = "Noida"
    total_accounts = 0
    next_account_number = 1001

    def __init__(self, name, balance, acc_type='Savings'):
        if BankAccount.is_valid_minimum_balance(balance):
            raise ValueError("The initial balance should not be less than Rs. 1000")
        BankAccount.total_accounts+=1
        self.acc_number = BankAccount.next_account_number
        BankAccount.next_account_number+=1
        self.name = name
        self.balance = balance
        self.acc_type = acc_type
        self.acc_creation = datetime.today()
        self.transactions = [f'Account created on {self.acc_creation.date()} with a balance of {balance}']

    def deposit(self, amount):
        self.balance+=amount
        self.transactions.append(f"Credited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance.\n")
        else:
            self.balance-=amount
            self.transactions.append(f"Debited {amount}")
    def details(self):
        print(f"Name: {self.name}\nAcc id: {self.acc_number}\nAcc type: {self.acc_type}\nBalance: Rs.{self.balance}\nRecent Transaction: {self.transactions[-1]}\nCreated on: {self.acc_creation}\n")

    def view_transaction_history(self):
        for i in self.transactions:
            print(i)
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


acc1 = BankAccount('Rahul', 10000)
acc1.details()
acc1.withdraw(2000)
acc1.deposit(3000)
acc1.withdraw(15000)
acc1.withdraw(1000)
acc1.details()

acc1.view_transaction_history()

acc2 = BankAccount('Ansh', 10000)
acc2.details()
acc3 = BankAccount('Ram', 10000)
acc3.details()

BankAccount.show_total_accounts()

BankAccount.show_bank_details()