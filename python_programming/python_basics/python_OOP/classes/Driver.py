class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_student(self):
        print(f"Name : {self.name} \nRoll # {self.roll}")


std1 = Student("nouman", 27)
std1.display_student()
