a = int(input("Enter coefficient A: "))
b = int(input("Enter coefficient B: "))
c = int(input("Enter coefficient C: "))
d = int(input("Enter coefficient D: "))
e = int(input("Enter coefficient E: "))
e = int(e)
for i in range(-e, d + e):
        if e % i == 0:
           f = (i**4*a) + (i**3*b) + (i**2*c) + (d*i) + e
           if f == 0:   
           
              print("Roots of quartic expansion are ",i)