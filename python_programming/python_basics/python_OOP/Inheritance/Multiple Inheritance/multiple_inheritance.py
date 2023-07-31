# diamond shape problem:
# In python multiple inheritance, if classes have same member, interpreter will
#    consider the first class member in the list if inherited classes


class A:
    def met(self):
        print("This is a method from class A")


class B(A):
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


class D(C, B):
    """ if both C and B class have same member, interpreter will
        consider the first class in the list if inherited classes """

    # def met(self):
    #     print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()
