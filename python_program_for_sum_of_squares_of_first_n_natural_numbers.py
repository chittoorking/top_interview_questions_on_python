print("This is python program to print sum of squares of first n natural numbers ")
n=int(input("Enter the number of natural numbers you want to sum by squaring"))
sum=0
def square(x):
    return x*x
for i in range(1,n+1):
    sum=sum+square(i)
print("Sum of squares of first n natural numbers is {0}".format(sum))