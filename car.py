class Car:

    def __init__(self,name,model,type,doors,wheels):
        self.name=name
        self.model=model
        self.type=type
        self.doors=doors
        self.wheels=wheels
    def car_properties(self):
        return (self.name,self.model,self.type,self.doors,self.wheels)

    @staticmethod
    def car_speed(distance,time):
        return int(distance/time)

car_1=Car('Belta','saloon','toyota',4,4)
print(car_1.car_properties())
print(car_1.car_speed(200,10))
