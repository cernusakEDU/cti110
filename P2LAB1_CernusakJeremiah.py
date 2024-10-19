# Jeremiah Cernusak
# 09/30/2024
# P2LAB1: 
# Determines circle values from given radius - diameter, circumfrence, and area.

#gather value of radius from user
radius = float(input("\nWhat is the radius of the circle?  "))

#diameter from radius = radius * 2
diameter = (radius * 2)
#rounded to nearest tenth
diameter = round(diameter, 1)

# circumfrence from radius = 2pi * radius | 2 * 3.141592653589793 * radius
circumfrence = (radius * 2 * 3.141592653589793)
#rounded to nearest hundredth
circumfrence = round (circumfrence, 2)

# area from radius = pi * radius | 3.141592653589793 * radius
area = radius * 3.141592653589793
#rounded to nearest thousandth
area = round (area, 3)

print ("\nThe diameter of the circle is", diameter)
print ("\nThe circumfrence of the circle is", circumfrence)
print ("\nThe area of the circle is", area,"\n")