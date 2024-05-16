# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
#V=πr2h=π·3.142·5≈154.87423
import math
pi=math.pi
radius = 3.14
height = 5
volume = pi*(radius**2)*height

print(round(volume,2))
