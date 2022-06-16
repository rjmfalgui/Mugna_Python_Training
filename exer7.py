class BankAccount:
    interest_rate = 0.3

    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)

    def deposit(self, amount):
        amount = int(amount)
        self.balance += amount
        print(f"New Balance after Deposit: {self.balance}")
        return self.balance
        
    def withdraw(self, amount):
        amount = int(amount)
        self.balance -= amount
        print(f"New Balance after Withdraw: {self.balance}")
        return self.balance

    def add_interest(self, interest):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"30% interest: {interest}")
        print(f"New Balance with interest: {self.balance}\n")
        return self.balance

class StudentAccount(BankAccount):
    def withdraw(self, amount):
        if int(amount) > 1000 or self.balance < int(amount):
            print("Withdraw amount too big")
        else:
            self.balance -= int(amount)
            print(f"New Balance after withdraw {self.balance}\n")

def main():
    name = input("Enter name: ")
    balance = input("\nEnter balance: ")

    acct = BankAccount(name = name, balance = balance)
    studAcct = StudentAccount(name = name, balance = balance)

    depAmount = input("\nEnter amount to deposit: ")
    acct.deposit(depAmount)

    widAmount = input("\nEnter amount to withdraw: ")
    acct.withdraw(widAmount)

    print("\nAdding interest\n")
    acct.add_interest(balance)

    print("*" * 25 + "\n")

    acctDepositAmount = input("Enter student account deposit amount: ")
    studAcct.deposit(amount = acctDepositAmount)

    acctWithdrawAmount = input("\nEnter student account withdraw amount: ")
    studAcct.withdraw(amount = acctWithdrawAmount)

    print("\nAdding interest\n")
    studAcct.add_interest(balance)

main()    # <-comment out if irun ang exer10 para mag run unittest 