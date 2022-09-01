#Write a python script to calculate simple interest

P = float(input("Enter the principal amount : "))
T = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))

SI = (P * T * R) / 100

print("Simple interest : " ,SI)
