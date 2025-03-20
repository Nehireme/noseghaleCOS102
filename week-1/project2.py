print("COMPOUND INTEREST")

P = float(input('Enter principle amount'))
R = float(input('Enter rate amount'))
T = float(input('Enter time period'))
n = float(input('Enter the number of times that interest is compounded '))

A = P*(1+(R/n)**(n*T))
print ("Compound interest is", A)
