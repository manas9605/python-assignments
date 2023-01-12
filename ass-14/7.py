'''Write a Python script to remove all non int values from a list.'''
a=print("enter elements in the list : ")
l1=[str(e) for e in input().split(',')]
l1=[e for e in l1 if e.isdigit()]
print("final list elements after removing non int values",l1)