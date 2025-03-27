a = float(input("Enter coefficient A: "))
b = float(input("Enter coefficient B: "))
c = float(input("Enter coefficient C: "))
d = float(input("Enter coefficient D: "))
d = int(d)
for i in range(1, d + 1):
       if d % i == 0:
           print(i) 
           f = lambda i: (i**3*a) + (i**2*b) + (i*c) + d 
           print(f(i))
           result = f(i)
           if result == 0:
            print(i)
           
           
print("Roots of cubic expansion are ")