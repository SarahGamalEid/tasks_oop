class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def seating_capacity(self,capacity):
        print( "the seating capacity is " ,capacity ," passengers")

class Bus(Vehicle):
    def fare(self):
        fare_bus = super().fare()
        fare_bus += fare_bus * (10 / 100)
        return fare_bus

School_bus = Bus("School Volvo", 12, 50)
School_bus.seating_capacity(50)
print("Total Bus fare is:", School_bus.fare())

print ("***************isinstance*************")
print(isinstance(School_bus, Vehicle))
print ("***************type*************")
print(type(School_bus))