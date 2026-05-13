#5-misol
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    def get_ram(self):
        return self.__ram

    def set_ram(self, new_ram):
        self.__ram = new_ram

l1 = Laptop('HP', 8)
print(l1.brand)
print(l1.get_ram())
l1.set_ram(16)
print(l1.get_ram())
