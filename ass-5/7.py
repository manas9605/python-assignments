#Write a python script which takes a three digit number from the user and displays
#only its last digit

a = str(input("enter a three digit no : "))
print("last digit of this no  is : ",a[-1])

#other method

a = int(input("enter a three digit no : "))
b=a%10
print("last digit of this no  is : ",b)