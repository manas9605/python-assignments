#Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots

print("enter coficient of x^2 : ")
a = int(input())
print("enter coficient of x : ")
b = int(input())
print("enter constant : ")
c = int(input())

D=b**2-4*a*c
print(D)
if   D>0:
    print("Real and distinct roots")
elif D==0:
    print("Real and equall roots")
else:
    print("imaginary roots")
