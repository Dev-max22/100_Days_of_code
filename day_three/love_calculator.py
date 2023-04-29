#Love_calculator
#name_input
print("Welcome to the love calculator!")
name_1 = input("What is your name? \n")
name_2 = input("What is your crush name? \n")
combined_name = name_1 + name_2
lower_case_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

Total_score = int(str(true) + str(love))

print(Total_score)

if Total_score < 10 or Total_score > 90:
    print(f"your score is {Total_score}, you are good to go like coke and mentors")
elif 40 <= Total_score <= 50:
    print(f"your score is {Total_score}, you are alright together")
else:
    print(f"Opps!, Your score is {Total_score},")

