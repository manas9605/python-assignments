#Write a python script which takes the radius from the user and display area of a circle.

a = float(input("enter radius : "))
b = 3.14* a**2
print("area of circle is : ",b)

#another way

from math import pi
a = float(input("enter radius : "))
b = pi* a**2
print("area of circle is : ",b)
