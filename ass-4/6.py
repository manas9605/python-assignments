#Write a python script to calculate the area of Triangle. Number is entered by the user

a = float(input("A : "))
b = float(input("B : "))
c = float(input("C : "))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area : ",area)
