print("This is python programme to print all primes in a given interval")
a,b=input("Enter the interval bounds to print the prime numbers in that interval").split()
a=int(a)
b=int(b)
count=0
for i in range(a,b+1):
    if(i==1):
        continue
    for j in range(2,int(i/2)+1):
          if i%j==0:
              count+=1
    if count>0:
        count=0
        continue
    else :
       print(i)
"""Definition: A prime number is a natural number greater than 1 that has no
positive divisors other than 1 and itself. The first few prime numbers are {2, 3,
5, 7, 11, ….}."""