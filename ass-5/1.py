#Write a python script to remove the last digit from a given number.

print("enter a no :")
a = str(input())
print("updated no is : ",a[:-1])

#other method


print("enter a no :")
a = eval(input())
print("updated no is : ",int(a/10))
