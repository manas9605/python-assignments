#Write a menu driven program to perform following operations - Addition, Subtraction,
#Multiplication, Division

print("1. Addition")
print("2. substraction")
print("3. multiplication")
print("4. division")
print("enter your choice : ")
choice=int(input())

match choice:
    case 1 :
        print("enter two nos : ")
        a,b = int(input()),int(input())
        c = a+b
        print("sum is : ",c)
    case 2:
        print("enter two nos : ")
        a,b = int(input()),int(input())
        c = a-b
        print("difference is : ", c)
    case 3:
        print("enter two nos : ")
        a,b = int(input()),int(input())
        c = a*b
        print("multiplication is : ", c)
    case 4:
        print("enter two nos : ")
        a,b = int(input()),int(input())
        c=a/b
        print("division is : ", c)
    case _:
        print("invalid input ")
print()
