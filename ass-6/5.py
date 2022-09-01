#Write a python script to print two given words in dictionary order

print("enter two words name : ")
a,b = input(),input()
x = min(a,b)
y = max(a,b)
print(x,y)

#other method

print("enter two words name : ")
c,d = input(),input()
print((d,c) if c>d else (c,d))