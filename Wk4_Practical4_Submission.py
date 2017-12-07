import random


class Vehicle:
    numbers = []

    def __init__(self,prefix):
        self.__prefix = prefix
        self.__register_number = random.randint(0,1000000)

    def get_register_number(self):
        while True:
            if self.__register_number in Vehicle.numbers:
                self.__register_number = random.randint(0,1000000)
            else:
                Vehicle.numbers.append(self.__register_number)
                self.__register_number = self.__prefix + str(self.__register_number)
                break
        return self.__register_number


class Bicycle(Vehicle):
    def __init__(self,prefix,gear_number):
        Vehicle.__init__(self,prefix)
        self.__gear_number = gear_number

    def get_gear_number(self):
        return self.__gear_number

    def set_gear_number(self,gear_number):
        self.__gear_number = gear_number

    def __str__(self):
        s = "Registration number: {} Gear number: {}".format(self.get_register_number(),self.get_gear_number())
        return s


class Skateboard(Vehicle):
    def __init__(self,prefix,board_length):
        Vehicle.__init__(self,prefix)
        self.__board_length = board_length

    def get_board_length(self):
        return self.__board_length

    def set_board_length(self,board_length):
        self.__board_length = board_length

    def __str__(self):
        s = "Registration number: {} SkateBoard length: {}".format(self.get_register_number(),self.get_board_length())
        return s


condition = "Y"
skateboards = {}
bicycles = {}
while condition.upper() =="Y":
    prefix = input("What is the vehicle type? (SK or BY) ")

    if prefix.upper() == "BY":
        gear_number = int(input("What is your gear number? "))
        B = Bicycle("BY",gear_number)
        print(B)
        bicycles[Bicycle.get_register_number(B)] = Bicycle.get_gear_number(B)

    elif prefix.upper() == "SK":
        board_length = float(input("What is your board length? "))
        S = Skateboard("SK",board_length)
        print(S)
        skateboards[Skateboard.get_register_number(S)] = Skateboard.get_board_length(S)
    else:
        print("Invalid vehicle type.")
    condition = input("Continue entering vehicles? (Y/N) ")

print("Skateboards: " + skateboards)
print("Bicycles: "+ bicycles)
