
from bank_accounts import *

Rachit = BankAccount(1000, "Rachit")
David = BankAccount(2000, "David")

Rachit.getBalance()
David.getBalance()

David.deposit(500)

Rachit.withdraw(10000)
Rachit.withdraw(10)

Rachit.transfer(10000, David)
Rachit.transfer(100, David)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Rachit)

Harry = SavingsAcct(1000, "Harry")

Harry.getBalance()

Harry.deposit(100)

Harry.transfer(10000, David)
Harry.transfer(1000, David)