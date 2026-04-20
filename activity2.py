class Vehicle:

    def __init__(self, maxspeed, mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
ModelX=Vehicle(240,18)
print("Car Model:  Tesla ModelX")
print("Mileage of Car: ", ModelX.mileage)
print("Maximum Speed of Car: ", ModelX.maxspeed)
