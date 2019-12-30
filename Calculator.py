import math
print('**Welcome to a Scientific calculator**')
print('Enter your choice \n1. Enter 1 to add two number\n2.Enter 2 to subtract the number\n3.Enter 3 to multiply three number\n4.Enter 4 to get the remainder\n5.Enter 5 to get the square root of a number ')

a=int(input('Enter first Number'))
b=int(input('Enter Second Number'))
ch=int(input('Enter your Choice'))
if ch==1:
    print('\n',a+b,'is the Sum Of two Number')
elif ch==2 and a>b:
    print('\n',a-b,'is the difference Of two Number')
elif ch==3:
    print('\n',a*b,'is the multiplication of Number')
elif ch==4:
    print('\n',a/b,'is the quotient of two Number')
else:
    print('Wrong Choice')
