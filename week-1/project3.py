print("ANNUITY PLAN")

PMT = float(input('Enter periodic payment amount'))
R = float(input('Enter rate amount'))
T = float(input('Enter time period'))
n = float(input('Enter the number of times that interest is compounded '))

A = PMT * (( (1 + R/n) ** (n*T) - 1 ) / (R/n))
print ("Annuity Plan is", A)
