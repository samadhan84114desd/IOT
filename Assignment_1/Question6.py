"""Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
epts the number as an argument
"""
def factorial(num):
    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i=i+1
    return fact
num=int (input("Enter positive number: "))
if num<0:
    print("Enter positive number")
else:
   factor= factorial(num)

print(f"factorial is ={factor}")
    