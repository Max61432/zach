class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        print(self.make, self.model)

class car(vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__( make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        print(self.make, self.model, self.fuel_type)

class rab:
    def __init__ (self, zp, grafik):
        self.zp = zp
        

x = car('bmw', 'm4', 'benz')
x.get_info()
