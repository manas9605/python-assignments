'''Write a python script to print first N even natural numbers in reverse order'''
a=int(input("enter a natural no : "))
for i in range(2*a,0,-2):
    print(i,end=' ')