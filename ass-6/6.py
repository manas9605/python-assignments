#Write a python script to check whether a given number is a three digit number or not

print("enter a no : ")
a = int(input())
if a<1000 and a>99:
    print("%d is a three digit no "%a)
else:
    print("%d is not a three digit no : "%a)

#other method

print("enter a no : ")
a = int(input())
if 1000>a>99:
    print("%d is a three digit no "%a)
else:
    print("%d is not a three digit no : "%a)