class BankException(Exception):
    pass


class BankAccount:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def getBalance(self):
        print(f"Hello {self.name} your balance is {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Successfully\n")
        self.getBalance()

    def LowBalance(self, amount):
        if (self.balance >= amount):
            return
        else:
            raise BankException(
                "\nPlease your balance is low to complete the transaction")

    def withDraw(self, amount):
        try:
            self.LowBalance(amount)
            self.balance = self.balance - amount
            print("Withdraw Successfully\n")
            self.getBalance()
        except Exception as error:
            print(f"Error: {error}")

    def transferMoney(self, amount, account):
        try:
            self.LowBalance(amount)
            self.balance = self.balance - amount
            account.deposit(amount)
            print("Transfer Successfully\n")
            self.getBalance()
        except Exception as error:
            print(f"Error: {error}")


class InterestBankAccount(BankAccount):
    def calculateInterest(self, interest, amount):
        return amount * (interest/100) + amount

    def deposit(self, amount):
        interest = self.calculateInterest(5, amount)
        self.balance = self.balance + interest
        print("Deposit Successfully\n")
        self.getBalance()


class SavingsAccount(InterestBankAccount):
    def __init__(self, balance, name):
        super().__init__(balance, name)
        self.fee = 5

    def withDraw(self, amount):
        try:
            self.LowBalance(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw Successfully\n")
            self.getBalance()
        except Exception as error:
            print(f"Error: {error}")
