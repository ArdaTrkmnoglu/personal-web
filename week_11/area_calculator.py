def triangle_area():
    base = int(input("Enter the base of the triangle: "))
    h = int(input("Enter the height of the triangle: "))
    area1 = 0.5 * base * h

    print(f"Area of the triangle is {area1}")


def circle_area():
    r = int(input("Enter the radius of the circle: "))
    pi = 3.14
    area2 = pi * r * r

    print(f"Area of the circle is {area2}")

    def cylinder_volume():
        h = int(input("Enter the height for the cylinder corresponding to this circle: "))
        vol = area2 * h
        print(f"Volume of the cylinder is {vol}")

    cylinder_volume()


def square_area():
    side = int(input("Enter the side of the square: "))
    area3 = side ** 2
    print(f"Area of the square is {area3}")

i = 10
print("Welcome to the area calculator program. \nThis program ise useful for finding the areas of significant shapes.")

while i > 0:
    print("1: Triangle")
    print("2: Circle (and volume of the corresponding cylinder)")
    print("3: Square")
    print("0: Exit")
    i = int(input(""))

    if i == 1:
        triangle_area()
    elif i == 2:
        circle_area()
    elif i == 3:
        square_area()