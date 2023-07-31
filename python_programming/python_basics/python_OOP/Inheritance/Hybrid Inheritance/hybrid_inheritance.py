# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.


# Python program to demonstrate
# hybrid inheritance

# Hybrid Inheritance
class vehicle:

    def __init__(self,model,mileage,price):
        self.price = price
        self.mileage = mileage
        self.model = model

    def show_details(self):
        print(f'Model : {self.model}')
        print(f'Price : {self.price}')
        print(f'Mileage : {self.mileage}')

class bike(vehicle):

    # Inherit Properties and Override
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.cc = cc
        self.tyre = tyre

    # Inherit Behavior and Override
    def show_details(self):
        super().show_details()
        print(f'CC : {self.cc}')
        print(f'Tyres : {self.tyre}')

    # Method of Derived Class
    def rating(self):
        print('4 star')


class car(bike,vehicle):

    def rating(self):
        print('5 star')

bajaj = bike("Dominar",40,145000,2,500)
tata = car("Safari",25,2500000,4,2000)

bajaj.show_details()
tata.show_details()

bajaj.rating()
tata.rating()
