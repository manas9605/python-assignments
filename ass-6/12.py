#Write a python script to accept one complex number from the user and display the
#greater number between real part and imaginary part
import xmlrpc.server

x = complex(input("enter a no "))
print (x.real) if x.real>x.imag else print(x.imag)
