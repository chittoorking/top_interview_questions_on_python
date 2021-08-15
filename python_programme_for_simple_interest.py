print("This is the pyhton programme to calculate simple interest")
P=float(input("Enter the principle amount"))
T=float(input("Enter the time"))
R=float(input("Enter the rate of interest"))
simple_interest=P*T*R/100
print("Simple interest for P={0} , T={1} and R={2} is {3}" .format(P,T,R,simple_interest))
