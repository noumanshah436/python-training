# duck typing = * concept where the class of an object is less important than the methods/attributes
#               * class type is not checked if the methods/attributes are present
#               * “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

# Using Duck Typing, we do not check types at all. Instead, we check for the presence of a
#            given method or attribute.
#  we can accept any object provided that the object have all the methods that are used by that object


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person():
    #  we can accept any object provided that the object have all the methods that are used here
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
