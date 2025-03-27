
def solve_quadratic(a, b, c):
    roots = np.roots([a, b, c])
    return roots

def solve_cubic(a, b, c, d):
    roots = np.roots([a, b, c, d])
    return roots

def solve_quartic(a, b, c, d, e):
    roots = np.roots([a, b, c, d, e])
    return roots

def main():
    print("Choose the type of equation to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        print("Roots:", solve_quadratic(a, b, c))
    elif choice == "2":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        print("Roots:", solve_cubic(a, b, c, d))
    elif choice == "3":
        a = float(input("Enter coefficient A: "))
        b = float(input("Enter coefficient B: "))
        c = float(input("Enter coefficient C: "))
        d = float(input("Enter coefficient D: "))
        e = float(input("Enter coefficient E: "))
        print("Roots:", solve_quartic(a, b, c, d, e))
    else:
        print("Invalid choice. Please run the program again.")
