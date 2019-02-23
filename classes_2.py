class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def calculate_perimiter(self):
        return (self.lenght*2) + (self.width *2)

class Square:

    square_list = []

    def __init__(self,s):
        self.side = s
        self.square_list.append(self.side)

    def calculate_perimiter(self):
        return self.side * 4

    def __repr__(self):
        return("{}".format(self.side))

def compare_objects(ob1, ob2):
    return ob1 is ob2


square = Square(4)
square2 = Square(6)

square3 = square2

print(Square.square_list)
print(square)

print(compare_objects(square2,square3))
    
