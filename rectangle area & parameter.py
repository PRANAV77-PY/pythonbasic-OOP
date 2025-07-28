class Rectangle:

    # function to pass width and length
    def __init__(self,width,length):
        self.width = width
        self.length = length

    #function to calculate area
    def area(self):
        return self.length * self.width
    
    #function to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)
    

#object creation
r = Rectangle(4,9)

#calling methods
print("Area: ",r.area())
print("Perimeter: ",r.perimeter())

#practice
class Rectangle:

    # function to pass width and length
    def __init__(self,length,width):
        self.length = length
        self.width = width

    #function to calculate area
    def area(self):
        return self.length * self.width
    
    #function to calculate area
    def perimeter(self):
        return 2 * (self.length + self.width)
    

#object craetion
r = Rectangle(2,6)

#calling method
print("area:",r.area())
print("perimeter:",r.perimeter())
    