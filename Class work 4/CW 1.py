class Figure:
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return  self.color

class Rectangle(Figure):
    def __init__(self, width, heith, color):
        self.width = width
        self.heith = heith
        self.color = Figure(color).get_color()
    def square(self):
        s = self.color
        result = str("square "+str(self.width*self.heith)+ " color:" + s)
        return result


class Square(Figure):
    def __init__(self, width, color ):
        self.width = width
        self.color = Figure(color).get_color()
    def square(self):
        s = self.color
        result = str("square: "+str(self.width*self.width)+ " color: " + s)
        return result



p = Square(10, "red").square()
print(p)
p2 = Rectangle(20,30, "green").square()
print(p2)