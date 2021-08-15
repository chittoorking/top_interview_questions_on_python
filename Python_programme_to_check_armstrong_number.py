print("This is python programme to check if a number is armstrong")
x=int(input("Enter a number to check if that number is armstrong or not"))
a=x
b=x
count=0
total=0
while(x>0):
    x=int(x/10)
    count+=1
for i in range(0,count):
    z=b%10
    b=int(b/10)
    total=total+z**count
if total==a:
    print("Yes {0}!It is an Armstrong number".format(a))
else:
    print("Sorry {0}!Its not an Armstrong number".format(a))