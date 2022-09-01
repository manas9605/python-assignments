#Write a python script to use NOT IN operator to display the data not present in list

list = ["mysirg","manas"]
s = 'saurav sir'
if s not in list:
     print(s, "is not present in the list")
else:
     print(s,"is present in the list")

#other method
l1=[1,3,5,7,9,10]
a=int(input("enter a no : "))
print(a not in l1)
