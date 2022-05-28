class Account(object):
    def __init__(self, number, balance, debt):
        self.number= number
        self.balance = balance
        self.debt = debt
    def check(self):
        print(f"Your account number {self.number} is in {self.balance}. You have {self.debt} a debt.")
    def debt_reset(self):
        self.debt = 0 
        print("Your debt has been reset!")
    def payment(self):
        x = int(input("Enter the amount you want to pay to the bank\n"))
        self.balance += x

def main():
    first = Account(1,1440, 23900)
    second = Account(2,1000, 1670)
    first.check()
    first.debt_reset()
    first.payment()
    first.check()
    second.payment()
    second.check()

main()
