#Write a python script to get the last digit from a given number. (for example, if user
#enters 2089 then your output should be 9)

a = str(input("enter a no : "))
print("last digit of the no is :",a[-1])

#other method

print("enter a no :")
a = eval(input())
print("updated no is : ",int(a%10))

