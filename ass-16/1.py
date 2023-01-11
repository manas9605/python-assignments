'''Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using tuple'''
print("Enter items to be stored in a tuple separated by comma : ")
t1=tuple([str(e) for e in input().split(',')])
print("tuple is : ",t1)