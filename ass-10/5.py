#Write a python script to print first N odd natural numbers in reverse order

a = int(input("enter a no : "))
for i in range(2*a-1,0,-2):
    print(i,end =' ')