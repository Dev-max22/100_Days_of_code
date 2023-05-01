# Lists in python

states_of_nigeria = ["Kwara", "Ogun", "Lagos", "Sokoto", "Nassarawa", "Kano", "Kaduna"]

# To append data to a list
states_of_nigeria.append("Yobe")
new_states = ["Kogi", "Imo", "Jiggawa"]
# To extend a list a
states_of_nigeria.extend(new_states)
print(states_of_nigeria)
# To print out a particular elements in a list
print(states_of_nigeria[7])
# To print out a particular elements in a list from the back use -ve indexing
print(states_of_nigeria[-4])
