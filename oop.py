class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def __str__(self):
        return f'This {self.capacity}oz coffee cup is {self.amount}oz full'
    
    def fill(self, fill_amount):
        self.amount += fill_amount

    def drink(self, drink_amount):
        self.amount -= drink_amount

    

gabes_cup = CoffeeCup(16)
abdallahs_cup = CoffeeCup(42)
westons_cup = CoffeeCup(24)

class Car():
    def __init__(self, make, model, year, speed = 0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f'vroom vroom, its my {self.year} {self.make} {self.model}'

    def accelerate(self, accel_amount):
        self.speed += accel_amount
    
    def brake(self, brake_amount):
        self.speed -= brake_amount

gabes_tesla = Car("Tesla", "Y", "1950")

print(gabes_tesla)