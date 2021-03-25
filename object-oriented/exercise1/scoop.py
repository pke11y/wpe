# Exercise 1 -
# Objected-Oriented course Rueven Lerner


class Scoop:
    def __init__(self, flavor: str) -> None:
        self.flavor = flavor

class Bowl(object):

    def __init__(self):
        self.bowl = []

    def add_scoop(self, s1, s2=None):
        self.bowl.append(s1)
        if s2:
            self.bowl.append(s2)

    def flavors(self):
        print(",".join([scoop.flavor for scoop in self.bowl]))


if __name__ == "__main__":
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("coffee")

    #print(s1.flavor)  # chocolate

    #for one_scoop in [s1, s2, s3]:
        # print(one_scoop.flavor)  # chocolate, vanilla, coffee

    b1 = Bowl()
    b1.add_scoop(s1, s2)
    b1.add_scoop(s3)
    b1.flavors()