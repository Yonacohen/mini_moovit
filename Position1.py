import math
class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcdist3(self, p):
        x = pow(self.x - p.x, 2)
        y = pow(self.y - p.y, 2)
        return math.sqrt(x + y)

    def print_pos(self):
        print("The location is " , self.x , self.y)








