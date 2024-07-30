import sys

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $  ")
tip = input("What percentage tip would you like to give? 5, 10, 12, or 15 (or other)? in %  ")
if int(tip) <= 0 or int(tip) > 100:
  print("Wrong tip % given")
  sys.exit()
  
people = input("How many people to split the bill? ")

total_bill = float(bill) * (1 + float(tip) / 100)
print("Total bill with tip: $ %.2f" % total_bill)

print("Amoung " + people + " people, each person should pay: $" + str(round(total_bill / int(people), 2)))