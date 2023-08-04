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


# <-------- INHERITANCE -------->

class Phone():
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'you have called {self.number}'

    def call(self, other_number):
        print(f'{self.number} is calling {other_number}')

    def text(self, other_number):
        print(f'{self.number} is texting {other_number}')

gabes_phone = Phone("6661234")






class iPhone(Phone):
    def __init__(self, number, generation, color, fingerprint = None):
        super().__init__(number)
        self.generation = generation
        self.color = color
        self.fingerprint = fingerprint

    def __str__(self):
        return f'ooh look at me, i have an iphone{self.generation} and its {self.color}'
    
    def set_fingerprint(self, digit):
        self.fingerprint = digit

    def unlock(self, input):
        if (self.fingerprint == input):
            print("welcome, phone unlocked!")
        else:
            print("invalid input, calling the cia")

gabes_iphone = iPhone("6661234", "14", "rose gold")

gabes_iphone.set_fingerprint("thumb")

class Android(Phone):
    def __init__(self, number, keyboard = "Default"):
        super().__init__(number)
        self.keyboard = keyboard

    def __str__(self):
        return f'This Android uses the {self.keyboard} keyboard.'
    
gabes_pixel = Android("6661234")

print(gabes_pixel)