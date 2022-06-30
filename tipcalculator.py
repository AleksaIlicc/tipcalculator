from unittest import result


print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
percetage = input("What percentage would you like to give? 10,12 or 15? ")
people = input("How many people to split the bill? ")
total_bill = float(total_bill)
people = int(people)
percetage = int(percetage)

res = (total_bill+(total_bill*percetage/100))/people
res = round(res, 2)
print(f"Each person should pay: ${res}")
