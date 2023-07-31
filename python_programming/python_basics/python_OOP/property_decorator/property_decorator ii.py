class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):  # getter method
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter  # setter method
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp = Employee("Nouman", "Shah")
print(emp.email)

emp.fname = "Farhan"
print(emp.email)

emp.email = "this.that@codewithharry.com"
print(emp.fname)

del emp.email
print(emp.email)

emp.email = "Harry.Perry@codewithharry.com"
print(emp.email)
