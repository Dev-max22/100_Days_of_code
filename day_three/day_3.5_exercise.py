"""This is a love calculator"""
print("Welcome to the love calculator!")
name_1 = input("What is your name?:\n")
name_2 = input("What is your crush name?:\n")

combined_name = name_1.lower() + name_2.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

first_digit = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

second_digit = l + o + v + e

love_score = str(first_digit) + str(second_digit)
love_score_as_int = int(love_score)
if (love_score_as_int <= 10) or (love_score_as_int >= 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score_as_int >= 40) and (love_score_as_int <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
