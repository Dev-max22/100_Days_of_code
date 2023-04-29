"""This contains a syntax on how to use the multiple if else statements"""
print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm?:"))
age = int(input("What is your age?:"))
if height >= 120:
    print("You can ride the roller-coaster")
    if age < 12:
        bill = 5
        print("Children tickets are $5")
    elif 12 < age < 18:
        bill = 7
        print("Youths tickets $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. YOu can have a ride with us!")
    else:
        bill = 12
        print("Adults tickets are $12")
    wants_photo = input("Do you want photos to be taken? Y or N:")
    if wants_photo == "Y":
        # Add $3 to their current bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")

