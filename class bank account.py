class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Account Created for {self.owner}")

    # function calculate 
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Deposit amount must be Positive")

    #function calculate
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdraw ${amount}")
        else:
            print("Insuffcient balance")

    #function Calculate
    def check_balance(self):
        print(f"Available balance: ${self.balance}")
        return self.balance


#Example usage
#object Creation
acc = BankAccount("Gourav",1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()