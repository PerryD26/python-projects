# Write your code below this line 👇
print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15, or 20? "))
bill_split = int(input("How many people to split the bill? "))
total_bill = bill * (tip/100) + bill
split_bill = round(total_bill / bill_split, 2)
print(f"Each person should pay: ${split_bill}")