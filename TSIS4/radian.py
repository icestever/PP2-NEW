import math
def degtorad(degrees):
    radians = degrees * (math.pi/180)
    return radians

deg = float(input("Input degree:"))

outputrad = degtorad(deg)

print("Output radian: ", outputrad)