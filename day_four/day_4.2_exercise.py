"""This file contains day_4.2 exercise"""
import random
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, separated by a comma: ")
names = namesAsCSV.split(",")
len_of_name = len(names)
# This gets a random names from the list
# random_choice = random.randint(0, len_of_name - 1)
# or
random_choice = random.choice(names)
who_will_pay = random_choice
# who_will_pay = names[random_choice]
print(f"{who_will_pay} is going to buy the meal today!")




