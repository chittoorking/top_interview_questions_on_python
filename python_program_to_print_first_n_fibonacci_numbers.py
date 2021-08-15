print("This is the python program to print first  n fibonacci numbers")
f=int(input("Enter the value for n to print first n fibonacci numbers"))
def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else :
        return fibonacci(x-1)+fibonacci(x-2)
print("First n fibonacci numbers are\n")
for i in range(1,f+1):
   n=fibonacci(i-1)
   print(n)
