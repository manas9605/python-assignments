'''Write a python script to calculate sum of first N odd natural numbers'''
a=int(input("enter a  no : "))
sum=0
for i in range(1,2*a,2):
    sum+=i
print(sum)