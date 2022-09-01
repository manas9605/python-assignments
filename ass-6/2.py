#Write a python script to check whether a given number is divisible by 5 or not
a = int(input("enter a no : "))
if a%5==0:
    print(a,"is div by 5")
else:
    print("%d is not div by 5"%a)

#single line method
print("no is div by 5" if int(input("enter a no : "))%5==0 else "no is not div by 5")