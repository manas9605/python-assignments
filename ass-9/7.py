#Write a python script to print first N even natural numbers in reverse order
print("enter a no : ")
n = int(input())

i=2*n
while(i>=2):
    print(i,end=' ')
    i-=2
