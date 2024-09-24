class Bird:
    def fly(self):
        print("fly with wings")


class Airplane:
    def fly(self):
        print("fly with fuel")


class Fish:

    def swim(self):
        print("fish swim in sea")


# ----------------------------------------
# Attributes having same name are
#   considered as duck typing
# for obj in Bird(), Airplane(), Fish():
#     obj.fly()


for obj in Bird(), Airplane() :
    obj.fly()
