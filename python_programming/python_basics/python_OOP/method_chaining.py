# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

# by default each method return None
# so in order to use method chaining ,
# return that current object using self keyword

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


# -----------------------------------

car = Car()


# car.turn_on().drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()
'''
    for readability , press enter after one method
    which will add line continuation char at the end
    and other methods move to a new line '''

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
