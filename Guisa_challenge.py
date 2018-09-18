name =input('What is your name? ')
hi = input('Hello '+ name +' Do you have a traingle for me? ')
if hi ==('yes'):
    print('yay')
a = int(input('Please enter side a: '))
b = int(input('Please enter side b: '))
c = int(input('Please enter side c: '))

if (a**2 + b**2 == c**2):
    print("this is a right triangle")
if (a**2 + b**2 < c**2):
    print("this is an obtuse triangle")
if (a**2 + b**2 > c**2):
    print("this is an acute triangle")
else:
    print("dis no triangle")