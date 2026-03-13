import numpy as np

class Circle():

    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return np.pi*np.pow(self.radius,2)
    
    def perimeter(self) -> float:
        return 2*np.pi*self.radius
    

if __name__=="__main__":

    circle = Circle(10)
    area = circle.area()
    perimeter = circle.perimeter()

    