class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        print("in __init__ method")

    @classmethod
    def from_dash(cls, string):
        print("in from_dash method")
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        #                    create object(cls for Employee)as we create normally and return it

        return cls(*string.split("-"))   # return object using *args method in single line


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

karan = Employee.from_dash("Karan-580-Student")    # make same object as above with
print(karan.salary)

# ****************************

# what we do in  from_dash method

# params = "Nouman-480-Student".split("-")
# print(params)  #  ['Nouman', '480', 'Student']
# obj = Employee(params[0], params[1], params[2])
# print(obj.salary)
