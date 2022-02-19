class Car:
    def __init__(self, year, make, model, fuel, doors):
        self.year = year
        self.make = make
        self.model = model
        self.fuel = fuel
        self.doors = doors

    def vehicle(self):
        description =    f'Year:          :{self.year}\n'\
                         f'Make:          :{self.make}\n'\
                         f'Model:         :{self.model}\n'\
                         f'Fuel:          :{self.fuel}\n'\
                         f'Doors:         :{self.doors}\n'\
        return description
