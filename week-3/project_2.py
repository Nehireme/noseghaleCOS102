print("ANNUAL TAX REVENUE FOR IZIFIN TECHNOLOGY")

age = int(input("Enter your age"))
years = int(input("Enter your years of work experience"))

if age >= 55 and years > 25:
 print("ATR OF STAFF IS N5,600,000")
elif age >= 45 and years > 20:
 print("ATR OF STAFF IS N4,480,000")
elif age >= 35 and years > 10:
 print("ATR OF STAFF IS 1,500,000")
elif age < 35 and years < 10:
 print("ATR OF STAFF IS  N550,000")
else:
 print("YOU DONT WORK HERE GET TF OUT!!!")
