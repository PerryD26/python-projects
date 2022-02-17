# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
total_bill = float(bill)
## total bill is now in floating data type
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_tip = int(tip)
## total tip is now in int data type 
bill_split = input("How many people to split the bill? ")
final_bill_split = int(bill_split)
## Need to calculate how much each person will need to pay. Round to the second decimal.
total_tip_bill = round(total_bill * (total_tip / 100) + total_bill, 2)
individual_total_bill = round(total_tip_bill / final_bill_split, 2)
print(f"Each person should pay: ${individual_total_bill}")
