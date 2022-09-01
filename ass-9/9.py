#Write a python script to print cubes of first N natural numbers
print("enter a no : ")
n = int(input())

i = 1
while(i<=n):
    print(i**3,end=' ')
    i+=1
print()