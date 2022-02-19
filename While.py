class Vehicle:
    def __init__(self, year, make, model, fuel, doors, trans):
        self.year = year
        self.make = make
        self.model = model
        self.fuel = fuel
        self.doors = doors
        self.trans = trans
    def ymm(self):
        description = f'Year: {self.year}\n' \
                      f'Make: {self.make}\n' \
                      f'Model: {self.model}\n'
        return description
    def fdt(self):
        info = f'Fuel: {self.fuel}\n' \
               f'Doors: {self.doors}\n' \
               f'Transmission: {self.trans}'
        return info
car1 = Vehicle('1998', 'Nissan', 'Sentra', 'Unleaded 87', 'Four doors', 'Automatic')
car2 = Vehicle('2001', 'Ford', 'Escort', 'Unleaded 87', 'Two Doors', 'Manual')
car3 = Vehicle('2013', 'Toyota', 'Prius V', 'Unleaded 87', 'Five Doors', 'Automatic')
car4 = Vehicle('2013', 'Hyundai', 'Elantra', 'Unleaded 87', 'Two Doors', 'Manual')
print(car1.ymm(), end=' ')
print(car1.fdt(), end=' ')
print()
print()
print(car2.ymm(), end=' ')
print(car2.fdt(), end=' ')
print()
print()
print(car3.ymm(), end=' ')
print(car3.fdt(), end=' ')
print()
print()
print(car4.ymm(), end=' ')
print(car4.fdt(), end=' ')
print()
print()
