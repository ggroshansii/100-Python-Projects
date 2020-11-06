#Tip calculator that accepts a bill total, adds tip, then divides based on group size

total = float(input("What was the total bill? "))
group_size = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 15, 20 or 25? "))

if tip == 15:
    final_amount = total * 1.15 / group_size
elif tip == 20:
    final_amount = total * 1.20 / group_size
elif tip == 25:
    final_amount = total * 1.25 / group_size
else:
    final_amount = total * (1.00 + (tip / 100)) / group_size

print(f"Each person should pay: {final_amount}")

