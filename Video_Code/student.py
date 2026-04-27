class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


#    @property
#    def name(self):
#        return self._name

#    @name.setter
#    def name(self, name):
#        if not name:
#            raise ValueError("Missing Name")
#        self._name = name

#    @property
#    def house(self):
#        return self._house

#    @house.setter
#    def house(self, house):
#        if house not in ["Pirates", "Revolutionaries", "Civilians", "Marines"]:
#            raise ValueError("Invalid House")
#        self._house = house


#    def charm(self):
#        match self.fruit:
#            case "Hito Hito no mi: Model Nika":
#                return "😆"
#            case "Hito Hito no mi":
#                return "🍄"
#            case "Hana Hana no mi":
#                return "🌸"
#            case _:
#                return "🍎"


def main():
    student = Student.get()
    #    if student["name"] == "Luffy":
    #        student["house"] = "Strawhats"
    #    print(f"{student['name']} from {student['house']}")
    # print(f"{student.name} from {student.house}")
    print(student)
    # print(student.charm())


# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)


#    student = {}
#    student["name"] = input("Name: ")
#    student["house"] = input("House: ")
#    return student


# name = input("Name: ")
# name = input("House: ")
# return {"name": name, "house": house}

if __name__ == "__main__":
    main()
