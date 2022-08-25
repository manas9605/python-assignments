#Write a python script to print greater among three numbers. Print number only once
#even if the numbers are the same.
print("enter three nos : ")
a,b,c = input(),input(),input()
x = max(a,b,c)
if(a==b and b==c):
    print(a)
else:
    print("greatest no is : ",x)