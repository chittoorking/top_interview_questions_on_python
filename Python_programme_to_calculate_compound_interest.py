print("This is python programme to find compound interest")
P=float(input("Enter the principle amount"))
T=float(input("Enter the number of units of time"))
R=float(input("Enter the rate of interest"))
Compound_interest=P*(1+R/100)*T
print("Compound interest for give P={0} ,T={1} and R={2} is CI={3}".format(P,T,R,Compound_interest))