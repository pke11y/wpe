# Exercise 1 -
# Objected-Oriented course Rueven Lerner
from bank_account import BankAccount

class Person:
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []
    
    def add_account(self, acc: BankAccount):
        self.accounts.append(acc)
    
    def all_balances(self):
        return [acc.balance() for acc in self.accounts]
    
    def current_total_balance(self):
        return sum(self.all_balances())
    
    def average_transaction_amount(self):
        return self.current_total_balance() / len(self.accounts)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone


if __name__ == "__main__":
    p1 = Person("Jake Kelly", "jk@pk.com", "12341234")
    p2 = Person("Cooper Kelly", "ck@pk.com", "34563456")
    p3 = Person("Sally Kelly", "sk@pk.com", "56785678")

    acc1 = BankAccount()
    acc2 = BankAccount()

    acc1.transactions.append(100)
    acc1.transactions.append(100)
    acc1.transactions.append(-50)
    print(sum(acc1.transactions))

    acc2.transactions.append(200)
    acc2.transactions.append(500)
    acc2.transactions.append(-50)

    # for p in [p1, p2, p3]:
    #     print(f"{p.name}, {p.phone} {p.email}")

    # p2.email = "cooper@pk.com"

    # for p in [p1, p2, p3]:
    #     print(f"{p.name}, {p.phone} {p.email}")
    
    p1.add_account(acc1)
    p1.add_account(acc2)

    print(p1.all_balances())
    print(p1.current_total_balance())
    print(p1.average_transaction_amount())