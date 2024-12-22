class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        print(self.make, self.model)

class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        print(self.make, self.model, self.fuel_type)



car = Car('Toyota', 'Land Cruiser', 'disel')

car.get_info()