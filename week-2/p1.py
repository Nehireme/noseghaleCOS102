print("Choose the type of equation to solve:")
print("1. Quadratic (Ax² + Bx + C = 0)")
print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
 a = float(input("Enter coefficient A: "))
 b = float(input("Enter coefficient B: "))
 c = float(input("Enter coefficient C: "))
 r1= -b+((b**2 - 4*a*c)**0.5)/(2*a)
 r2= -b-((b**2 - 4*a*c)**0.5)/(2*a)
 print("Roots of quadratic are", r1)
 print("and ", r2)

if choice == "2":
 a = float(input("Enter coefficient A: "))
 b = float(input("Enter coefficient B: "))
 c = float(input("Enter coefficient C: "))
 d = float(input("Enter coefficient D: "))
 d = int(d)
 for i in range(1, d + 1):
       if d % i == 0:
           f = (i**3*a) + (i**2*b) + (i*c) + d 
           if f == 0:
            print("Roots of cubic expansion are ",i)  

if choice == "3":
 a = float(input("Enter coefficient A: "))
 b = float(input("Enter coefficient B: "))
 c = float(input("Enter coefficient C: "))
 d = float(input("Enter coefficient D: "))
 e = float(input("Enter coefficient E: "))
 print("Roots of quartic expansion are ")