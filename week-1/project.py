print("SIMPLE INTEREST")

P = float(input('Enter principle amount'))
R = float(input('Enter rate amount'))
T = float(input('Enter time period'))

A = P*(1+(R/100)*T)
print ("Simple interest is", A)
