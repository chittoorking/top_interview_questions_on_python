def calculateFactorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*calculateFactorial(x-1)
print("This is a programme for calculating factorial of a number")  
a=int(input("Enter a number to find factorial of it") )
factorial=calculateFactorial(a)
print("Factorial of {0} is {1}".format(a,factorial))
