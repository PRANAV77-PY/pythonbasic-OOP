import math

# define Main function
def circle_area_perimeter(radius):
    if radius < 0:
        return "Radius cannot be negative"
    

    # define a value calculation in area
    area = math.pi * radius ** 2

    #define a value calculation in perimeter
    perimeter = 2 * math.pi * radius

    return area,perimeter

#Example usage
r = 5
a,p = circle_area_perimeter(r)
print(f"Radius:{r}")
print(f"Area: {a:2f}" )
print(f"perimeter:{p:2f}")
