'''Write a python script to calculate sum of digits of a given number'''
a=int(input("enter a no : "))
sum=0
while(a>0):
    sum=sum+a%10
    a=a//10
print(f"sum of digits of no is {sum} ")

'''a=int(input("enter a no : "))
sum=0
for i in range(b):
    sum+=i
print(f"sum of digits of {a} is {sum}")
'''

