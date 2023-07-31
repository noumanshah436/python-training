
class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
print(emp_1.email)
print(emp_1.fullname)

# output:
# Created Employee: John Smith - John.Smith@email.com
# John.Smith@email.com
# John Smith
