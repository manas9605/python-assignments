#Write a python script to print first N natural numbers in reverse order

a = int(input("enter a no : "))
for i in range(a):
    print(a-i,end =' ')

#another method
a = int(input("enter a no : "))
for i in range(a,0,-1):
    print(i,end=' ')