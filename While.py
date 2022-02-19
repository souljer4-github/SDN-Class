class Vehicle:
    def __init__(self, year, make, model, fuel, doors):
        self.year = year
        self.make = make
        self.model = model
        self.fuel = fuel
        self.doors = doors

    def info(self):
        description = f'Year: {self.year}\n' \
                      f'Make: {self.make}\n' \
                      f'Model: {self.model}\n' \
                      f'Fuel: {self.fuel}\n' \
                      f'Doors: {self.doors}\n'
        return description


car1 = Vehicle('1998', 'Nissan', 'Sentra', 'Unleaded 87', 'Four doors')
car2 = Vehicle('2001', 'Ford', 'Escort', 'Unleaded 87', 'Two Doors')
car3 = Vehicle('2013', 'Toyota', 'Prius V', 'Unleaded 87', 'Five Doors')
car4 = Vehicle('2013', 'Hyundai', 'Elantra', 'Unleaded 87', 'Two Doors')

print(car1.info())
print(car2.info())
print(car3.info())
print(car4.info())
