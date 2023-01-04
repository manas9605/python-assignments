'''Write a python script to calculate sum of cubes of first N natural numbers'''
a = int(input("enter a no : "))
sum=0
for i in range(1,a+1):
    sum+=i**3
print(sum)