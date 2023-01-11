'''Write a python program to check if all items in the tuple are the same.'''
print("Enter items to be stored in a tuple separated by comma : ")
t1=tuple([str(e) for e in input().split(',')])
if t1[0]*len(t1)==t1:
    print("tuple has same elements")
else:
    print("tuple doesnot has same elements")