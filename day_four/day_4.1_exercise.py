"""This code contains the heads or tail exercise"""
import random
# Don't touch the code below
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)
# Don't touch the code above

# Write your code below this line
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
