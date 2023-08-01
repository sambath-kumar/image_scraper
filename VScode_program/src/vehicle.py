class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def disp(self):
        print(f"The brand is {self.brand} and model is {self.model}")