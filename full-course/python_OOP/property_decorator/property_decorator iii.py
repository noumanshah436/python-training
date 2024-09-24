class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property         # after decorating we can only use it as an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')


print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)

emp_1.fullname = "Syed Nouman"


print()
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)


# del emp_1.fullname
