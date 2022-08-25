#Write a python script to store a hexadecimal number 2F in a variable and print it in
#octal format.

a = input("enter a hexadecimal no : ")
dec_no = int(a,16)
oct_no = oct(dec_no)
print("decimal no : ",dec_no)
print("octal conversion of no is : ",oct_no)

#other method
''' 
x = 0x2F
print(oct(x))
'''