#task1
import math
degree = int(input("Input degree: "))
radian = math.radians(degree)
print("Output radian: ", radian)

#task2
height = int(input("Height: "))
base1 = int(input("Base, first value: " ))
base2 = int(input("Base, second value: "))
area = ((base1 + base2)/2)*height
print("Expected output: ", area)

#task3
import math
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
ap = length/(2*(math.tan(math.pi/sides)))
area = int((sides*length*ap)/2)
print("The area of the polygon is: ", area)

#task4
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = float(base*height)
print("Expected Output: ", area)