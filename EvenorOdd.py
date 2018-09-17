"""
Write a program that will take a number (integers only) and 
return a statement that will let the user know if it is even or odd
"""
num = int(input("number plz "))
if (num%2) == int("1"):
    print("this number is odd")
if (num%2) == int("0"):
    print ('this number is even')
    
