#Write a python script to swap data of two variables

print("enter two variables x & y : ")
x,y=input(),input()
temp = x
x = y
y = temp

print("value of x after swapping is : ",x)
print("value of y after swapping is : ",y)

#other method
print("enter two variables x & y : ")
x,y=input(),input()

x,y=y,x

print("value of x after swapping is : ",x)
print("value of y after swapping is : ",y)
