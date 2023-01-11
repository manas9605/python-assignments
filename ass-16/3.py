'''Write a python program to reverse the tuple.'''
print("Enter items to be stored in a tuple separated by comma : ")
t1=tuple([str(e) for e in input().split(',')])
print("reverse of the tuple is : ",t1[::-1])
