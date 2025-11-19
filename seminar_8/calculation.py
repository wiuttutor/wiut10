import math
def calculation(radius):
    diameter = radius *2
    circum = 2 * math.pi * radius
    area = math.pi * pow(radius, 2)

    return f"Diameter: {diameter}\nCircum: {circum}\nArea: {area}"

print(calculation(2))