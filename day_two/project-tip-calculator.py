# This is a project tip claculator
print("Welcome to the tip claculator")
total_bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
tip_in_percentage = 1 + (tip / 100)
num_of_people = int(input("How many people should split the bill?: "))
each_person_bill = (total_bill / num_of_people) * tip_in_percentage
print(f"Each person should pay: ${round(each_person_bill, 2)}")

