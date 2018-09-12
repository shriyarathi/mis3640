# Define a function quadratic(a, b, c) to solve a quadratic equation:
# ax**2+bx+c=0

import math
a = 1
b = 5 
c = 6


a = int(input("Enter the coefficients of a: "))
b = int(input("Enter the coefficients of b: "))
c = int(input("Enter the coefficients of :c "))

d = (b**2) - (4*a*c)

s1 = (-b-math.sqrt(d))/(2*a)
s2 = (-b+math.sqrt(d))/(2*a)

print('Solution are {} and {}'.format(s1,s2))
