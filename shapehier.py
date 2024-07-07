class Shape():
    def __init__(self, color):
        self.color = color
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area()")

        
    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement calculate_perimeter()")
    
    def get_color(self):
        return self.color
    def set_color(self):
        try:
            self.color =  str(input("Please enter new color please. : "))
            return self.color
        except:
            return print(f"Sorry but the color you entered could not be saved, be sure to enter one word with only letters please.")
        

    
class Triangle(Shape):
    def __init__(self, color, sideone, sidetwo, sidethree):
        super().__init__(color)
        self.sideone = sideone
        self.sidetwo = sidetwo
        self.sidethree = sidethree

    def calculate_perimeter(self):
        return self.sideone + self.sidetwo + self.sidethree
    def calculate_area(self):
        return (self.sideone + self.sidetwo + self.sidethree) / 2

        

class Rectangle(Shape):
    def __init__(self, color, width, length):
        super().__init__(color)
        self.width = width
        self.length = length
    def calculate_area(self):
        return self.length * self.width
        
        
    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width
        
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
      
    def calculate_area(self):
        pie = 3.14159
        return pie * self.radius * self.radius
        
        
    def calculate_perimeter(self):
         pie = 3.142
         return 2 * pie * self.radius
        
# had to use gemini on the code below couldn't figure out how to use the functions above correctly, so it seems in order to invoke these functions they data/input has to be set up before you can use them properly.
if __name__ == "__main__":
    triangle = Triangle("blue", 3, 4, 5)
    rectangle = Rectangle("red", 5, 10)
    circle = Circle("green", 4)
# ^ i was doing this wrong, I trying to use print(Circle.calculate_arena(5)) and yeah wasn't working
    shapes = [triangle, rectangle, circle]

    for shape in shapes:
        print(f"Shape: {shape.__class__.__name__}")  
        print(f"  Color: {shape.get_color()}")
        print(f"  Area: {shape.calculate_area()}")
        print(f"  Perimeter: {shape.calculate_perimeter()}")
        print("---")
