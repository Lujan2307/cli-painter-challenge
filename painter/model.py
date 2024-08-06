# TODO: Add code here
import math

import matplotlib as plt

class point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __init__(self, center: point, radius:float):
        self.radius:float =radius
        self.center:point = center


    def area_Circle(self)->float:
        Area = math.pi*(self.radius)**2
        return Area

    def Draw(self):
        circle = plt.Circle( xy: (self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()