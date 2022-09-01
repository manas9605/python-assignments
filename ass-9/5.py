#Write a python script to print first N odd natural numbers in reverse order
print("enter a no : ")
n = int(input())

i = 1
while(i<=2*n):
    print((2*n)-i,end=' ')
    i+=2