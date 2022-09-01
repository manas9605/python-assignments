#Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same.
a = int(input("enter a no :"))
b = int(input("enter other no :"))
if a>b:
    print("%d is grater"%a)
else:
    print(a)

#other method
print("enter two no :")
c,d=int(input()),int(input())
print(c if c>d else d)