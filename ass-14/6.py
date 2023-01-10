'''Write a Python script to calculate the sum of elements in a given list of numbers.'''

a=print("enter elements separated by comma : ")
l1=[int(i) for i in input().split(',')]
b=sum(l1)
print("the sum of elements of the given list is : ",b)