"""This is a pizza order coding exercise"""
# Angela_yu "Code"
print("Welcome to python pizza deliveries")
size = input("Which size do you want? S, M or L:")
add_pepperoni = input("Do you want pepperoni? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N:")
bill = 0
if size == "S":
    # Add $15 to their bill
    bill += 15
elif size == "M":
    # Add $20 to their bill
    bill += 20
elif size == "L":
    # Add $25 to their bill
    bill += 25
else:
    print("You have entered a wrong input")


if add_pepperoni == "Y":
    if size == "S":
        # Add $2 to their current bill
        bill += 2
    else:
        # Add $3 to their current bill
        bill += 3
if extra_cheese == "Y":
    bill += 1
else:
    print(f"your final bill is ${bill}")


# My_implemented code
# print("Welcome to python pizza deliveries")
# size = input("Which size do you want? S, M or L:")
# add_pepperoni = input("Do you want pepperoni? Y or N:")
# extra_cheese = input("Do you want extra cheese? Y or N:")
# bill = 0
# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
#     else:
#         bill += 0
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill += 0
#     print(f"Your final bill is ${bill}")
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
#     else:
#         bill += 0
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill += 0
#     print(f"Your final bill is ${bill}")
# elif size == "L":
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
#     else:
#         bill += 0
#         if extra_cheese == "Y":
#             bill += 1
#         else:
#             bill += 0
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("You have entered a wrong input!")
