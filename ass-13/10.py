'''Write a Python script to create a list, where each element of the list is a digit of a
given number'''
print("enter digits of a no separating comma : ")
l1=[eval(i) for i in input().join(',')]
print("the final given no is : ",l1)