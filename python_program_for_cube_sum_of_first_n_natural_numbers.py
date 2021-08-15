print("This is python program to print sum of cubes of first n natural numbers ")
n=int(input("Enter the number of natural numbers you want to sum by cubing"))
sum=0
def cube(x):
    return x**3
for i in range(1,n+1):
    sum=sum+cube(i)
print("Sum of cubes of first n natural numbers is {0}".format(sum))