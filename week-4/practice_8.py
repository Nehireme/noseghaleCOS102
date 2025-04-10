total = 50;
def sun(arg1,arg2):
 total = arg1+arg2;
 print("inside the function loocal total:", total)
 return total;

sum(10,20);
print("outside the function global total:",total)