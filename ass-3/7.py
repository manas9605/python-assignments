#Write a python script to store binary number 1100101 in a variable and print it in
#decimal format

binary_num= input('Enter a binary to convert into decimal:')
decimal_num= int(binary_num, 2)
octal_num = oct(decimal_num)
print("decimal no :",decimal_num)
print('Octal number representation is:', octal_num)

#other method
'''
x=0b1100101
print(x)
'''