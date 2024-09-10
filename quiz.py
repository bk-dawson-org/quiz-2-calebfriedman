import math

radius = float(input("Give me the radius of a sphere and I'll find its volume: "))

volume = 4*math.pi*radius**2/3

answer = round(volume, 4) #Rounding it to four decimal places

print("Its volume is around", answer)
