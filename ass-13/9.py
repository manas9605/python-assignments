'''Write a Python script to create a list of city names taken from the user.'''
print("enter city names separated by comma  : ")
l1=[str(e) for e in input().split(',')]
print(f"city names entered by the user are : {l1}")
