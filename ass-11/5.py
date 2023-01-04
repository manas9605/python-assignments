#Write a python script to calculate sum of first N even natural numbers
a=int(input("enter a  no : "))
sum=0
for i in range(2,2*a+1,2):
    sum+=i
print(sum)