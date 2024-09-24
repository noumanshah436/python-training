class Car:
    wheels = 4  # class variable

    def __init__(self,make,model,year,color):
        self.make = make        # instance variable
        self.model = model      # instance variable
        self.year = year        # instance variable
        self.color = color      # instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


'''
1) if we change class variable using class name, it will change for all object
2) if we change class variable using object name , it will change only for that object

'''

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

Car.wheels = 2
car_1.wheels = 4

car_1.model = "suzuki"
print(car_1.wheels)
print(car_2.wheels)

print(car_1.make)
print(car_1.year)
print(car_1.color)
print(car_1.model)

car_1.drive()
car_2.stop()
