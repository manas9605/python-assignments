#Write a python script to check whether a given number is even or odd

a = int(input("enter a no :"))
if a%2==0:
    print("even")
else:
    print("odd")

#songle line
print("odd" if int(input("enter a no : "))%2==0 else "even")