'''Write a python program to check whether a given string is a multiword string or single
word string using match case statement'''

a = str(input("enter a string : "))
a.strip() #it will undo initial spaces in a string
match a:
    case a if ' ' in a :
        print("multiword string")
    case a if ' ' not in a:
        print("single word string")