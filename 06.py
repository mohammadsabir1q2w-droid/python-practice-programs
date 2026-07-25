import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

print("x2 - x1=", x2 - x1)
print("y2 - y1=", y2 - y1)

print("(x2 - x1) ** 2=", (x2 - x1) ** 2)
print("(y2 - y1) ** 2=", (y2 - y1) ** 2)

total = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
print("Total=", total)

distance = math.sqrt(total)
print("Distance=", distance)