print("This is the python program to calculate nth fibonacci number")
f=int(input("Enter the value for n to find n'th fibonacci number"))
def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else :
        return fibonacci(x-1)+fibonacci(x-2)
n=fibonacci(f)
print("nth fibonacci number is {0}".format(n))
