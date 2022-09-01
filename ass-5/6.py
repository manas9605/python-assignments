#Write a python script which takes a three digit number from the user and displays
#only its middle digit

a = str(input("enter a three digit no : "))
print("middle digit of this no  is : ",a[1])

#other methods
a = int(input("enter a three digit no : "))
num=int(a/10)
num_middle=int(num%10)
print("middle digit of this no  is : ",num_middle)