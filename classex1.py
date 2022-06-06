class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def mycar(self):
        print("max speed is %d and mileage is %d" %(self.max_speed,self.mileage))
anu_car=Vehicle(100,28)
anu_car.mycar()
arun_car=Vehicle(110,30)
arun_car.mycar()