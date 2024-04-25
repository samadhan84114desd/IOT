# Using for loop, write and run a Python program to find factorial from 0 to 10.

def factorial(num):
    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i=i+1
    return fact
i=0
while(i<=10):
   factor= factorial(i)
   print(f"factorial of {i} is {factor}")
   #print(f"factorial is ={factor}")
   i=i+1