#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

data = int(input("Enter the radius: "))
data2 = int(input("Enter the height: "))
aa = math.pi*math.pow(data,2)
b = int(math.pow(data2,2))
a = int(math.pow(data,2))
c = math.sqrt(a + b)
m = math.pi*data*c
g = math.pi*math.pow(data,2)
g = math.pi*math.pow(data,2)
surfacearea = m + g
print(f"The surface is {surfacearea}.")