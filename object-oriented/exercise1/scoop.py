# Exercise 1 -
# Objected-Oriented course Rueven Lerner


class Scoop:
    def __init__(self, flavor: str) -> None:
        self.flavor = flavor


if __name__ == "__main__":
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("coffee")

    print(s1.flavor)  # chocolate

    for one_scoop in [s1, s2, s3]:
        print(one_scoop.flavor)  # chocolate, vanilla, coffee
