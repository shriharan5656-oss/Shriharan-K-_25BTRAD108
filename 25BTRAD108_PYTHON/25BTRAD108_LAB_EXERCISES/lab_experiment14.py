class BankAccount:
    def __init__(self, acc_no, name, bal=0.0):
        self.acc_no, self.name, self.__bal = acc_no, name, max(0.0, float(bal))

    def deposit(self, amt):
        if amt <= 0: return print(f"Invalid deposit: ${amt}")
        self.__bal += amt
        print(f"Deposited ${amt:.2f}. Balance: ${self.__bal:.2f}")

    def withdraw(self, amt):
        if 0 < amt <= self.__bal:
            self.__bal -= amt
            print(f"Withdrew ${amt:.2f}. Balance: ${self.__bal:.2f}")
        else:
            print(f"Withdrawal rejected: ${amt:.2f}")

    def show(self):
        print(f"[{self.acc_no}] {self.name} | Balance: ${self.__bal:.2f}")

if __name__ == "__main__":
    acc = BankAccount("ACC-109284", "Shriharan K", 500)
    acc.show()
    acc.deposit(250)
    acc.withdraw(150)
    acc.withdraw(700)
    acc.deposit(-50)
    acc.show()
