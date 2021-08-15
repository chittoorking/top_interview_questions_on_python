import math
print("This is a python programme to check if a given number is a fibonacci number or not")
a=int(input("Enter a number to check if it is a fibonacci number or not"))
def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isFibonacci(a):
    return isPerfectSquare((5*a**2)+4) or  isPerfectSquare((5*a**2)-4)
x=isFibonacci(a)
if x==True:
    print("Yes ! It is a fibonacci number ")
else :
    print("No ,it is not a fibonacci number ")