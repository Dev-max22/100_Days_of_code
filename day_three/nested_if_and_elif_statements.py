# For a nested if statement this is the format
# if condition:
#   if condition:
#       print("Do this")
#   else:
#       print("Do this")
# else:
#   print("Do that")
# example of a nested-if statement
print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm?:"))
age = int(input("What is your age?:"))
if height >= 120:
    print("You can ride the roller-coaster")
    if age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")
# example of an elif statement
print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm?:"))
age = int(input("What is your age?:"))
if height >= 120:
    print("You can ride the roller-coaster")
    if age < 12:
        print("Please pay $5")
    elif 12 < age < 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")

