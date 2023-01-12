'''Write a python program to multiply all the numbers in a list.'''

def a(list):
    mul=1
    for i in list:
        mul*=i
    print("mul is : ",mul)
ele=[1,2,3,4,5]

a(ele)