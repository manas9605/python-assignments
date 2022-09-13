'''Write a python program to check whether a given number is positive, negative or
zero using match case statement'''

a = int(input("enter a no : "))
match a:
    case a if a >0:
        print("no is positive")
    case a if a<0:
        print("no is negative")
    case a if a==0:
        print("no is zero")