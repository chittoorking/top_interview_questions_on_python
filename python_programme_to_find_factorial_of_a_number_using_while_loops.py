print("This is python programme to find factorial of a number using loops ")
a=int(input("Enter an inter to find the factorial of it"))
x=a
factorial=1
while(x>=0):
    if x==0:
        factorial=factorial*1
        break
    elif x==1:
        factorial=factorial*1
        x-=1
    else :
        factorial=x*factorial
        x-=1
print("Factorial of given integer {0} is {1}".format(a,factorial))