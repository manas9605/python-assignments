#Write a python script to print greater among three numbers. Print number only once
#even if the numbers are the same.
print("enter three nos : ")
a,b,c = input(),input(),input()

max = a if a>b else b
maxi = c if c>max else max

if(a==b and b==c):
    print(a)
else:
    print("greatest no is : ",maxi)

#other method

print("enter three nos : ")
d,e,f = input(),input(),input()

print((a if a>c else c) if a>b else (b if b>c else c))

#Another method

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)