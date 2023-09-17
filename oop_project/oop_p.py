from bank import *

Rogers = BankAccount(1000, "Rogers")
Cathy = BankAccount(2000, "Cathy")

Rogers.withDraw(300)
Rogers.deposit(100)

Rogers.transferMoney(800, Cathy)
Cathy.transferMoney(900, Rogers)

Wandera = InterestBankAccount(1000, "Wandera")

Wandera.deposit(500)

Test = SavingsAccount(1000, "Test")
Test.deposit(1000)

Test.withDraw(500)
