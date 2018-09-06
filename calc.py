import math
import time

print(math.pi)

radius = 5
volume = (4.0/3.0) * math.pi * radius**3.0

print ('The volume of a sphere with radius = {rad} is  {vol}'.format(rad=radius, vol=volume))


copies = 60

wholesalecost = (24.95*.6* copies)+ (copies*.75) + 3

print ('The wholesale cost for = {cop} is  {who}'.format(cop=copies, who=wholesalecost))

iv = 82
fv = 89

increase = ((fv-iv)/iv)*100.0

print ('The percentage increase for {} to {} is {}%'.format(iv, fv, increase))