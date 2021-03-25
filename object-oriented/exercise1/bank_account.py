# Exercise 1 -
# Objected-Oriented course Rueven Lerner


class BankAccount(object):
    def __init__(self, transactions=[]) -> None:
        self.transactions = transactions

    def balance(self):
        return sum(self.transactions)
    
    def average(self):
        return self.balance / len(self.transactions)
    # @property
    # def transactions(self) -> list:
    #     return self._transactions

    # @transactions.setter
    # def transactions(self, trans: list):
    #     self._transactions = trans

    # def deposit(self, amount: float):
    #     """
    #     Every time you deposit, append a positive float

    #     Args:
    #         amount (float): deposit to account
    #     """
    #     self._transactions.append(amount)

    # def withdraw(self, amount: float):
    #     """
    #     Every time you withdraw, append a negative float

    #     Args:
    #         amount (float): withdraw amount
    #     """
    #     self._transactions.append(-amount)

    # def __str__(self) -> str:
    #     return f"Avg: {self._avg()} Balance:{self._sum()} Number of Transactions: {self._number_of_transactions()}"

    # def _avg(self) -> float:
    #     return sum(self.transactions) / len(self.transactions)

    # def _sum(self) -> float:
    #     return sum(self.transactions)

    # def _number_of_transactions(self) -> float:
    #     return len(self.transactions)


if __name__ == "__main__":
    acc1 = BankAccount()
    acc2 = BankAccount()

    acc1.transactions.append(100)
    acc1.transactions.append(100)
    acc1.transactions.append(-50)
    print(sum(acc1.transactions))

    acc2.transactions.append(200)
    acc2.transactions.append(500)
    acc2.transactions.append(-50)
    print(sum(acc2.transactions))
    print(sum(acc2.transactions) / len(acc2.transactions))
    # acc1.deposit(5)
    # acc1.deposit(10)
    # acc1.deposit(25)
    # acc1.withdraw(10)

    # acc2.deposit(55)
    # acc2.deposit(100)
    # acc2.deposit(250)
    # acc2.withdraw(100)

    # print(acc1)
    # print(acc2)