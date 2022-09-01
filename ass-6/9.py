#Write a python script to check whether a given year is a leap year or not
a = int(input("enter a year "))
print("leap year" if a%400==0 else "leap year" if a%4==0 and a%100!=0 else "not a leap year")

#other method

year = int(input("enter a year "))
if year%400==0 or year%100!=0 and year%4==0:
    print("leap year")
else:
    print("nin leap year")