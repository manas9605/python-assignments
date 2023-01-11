'''Write a python program to store your own information {name, age, gender, so on..}'''
print("enter your name , age ,gender , highest qualification using comma  : ")
s1={str(e) for e in input().split(',')}
print("my own info : ",s1)