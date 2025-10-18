

# Create a class Vehicle with attributes brand and model. Derive Car and Bike subclasses with specific attributes. 
# Implement a method to display details of each vehicle.



class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print("V_Brand:", self.brand)
        print("V_Model:", self.model)
# c=Vehicle("Honda","City")
# c.display_details()

class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors
    def display_details(self):
        print("Car Brand is:",self.brand)
        print("Car Model is:",self.model)
        print("Number of Doors:",self.number_of_doors)

     
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type  # e.g., 'Sport', 'Cruiser'
    def display_details(self):
        print("Bike Brand is:",self.brand)
        print("Bike Model is:",self.model)
        print("Bike Type:",self.bike_type)


C1=Car("Toyota", "Camry", 4)
print("Car Details:")
C1.display_details()
c2=Bike("Yamaha", "MT-15", "Sport")
print("\nBike Details:")
c2.display_details()    


# Output:
# Car Details:
# Car Brand is: Toyota
# Car Model is: Camry
# Number of Doors: 4

# Bike Details:
# Bike Brand is: Yamaha
# Bike Model is: MT-15
# Bike Type: Sport