import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):             # cls is class not using self so that it's not changeable or something idk
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
