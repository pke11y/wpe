# Exercise 1 -
# Objected-Oriented course Rueven Lerner


class Person:
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone

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

    for p in [p1, p2, p3]:
        print(f"{p.name}, {p.phone} {p.email}")

    p2.email = "cooper@pk.com"

    for p in [p1, p2, p3]:
        print(f"{p.name}, {p.phone} {p.email}")