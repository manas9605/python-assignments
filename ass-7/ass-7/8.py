'''Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''
s1 = input("enter a string : ")
s2 = input("enter other string : ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("identical strings")
    case (s1,s2) if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {}".format(s2,s1))
