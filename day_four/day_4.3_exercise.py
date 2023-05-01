"""This file contains day_4.3 exercise"""
row_1 = ["🤑", "🤑", "🤑"]
row_2 = ["🤑", "🤑", "🤑"]
row_3 = ["🤑", "🤑", "🤑"]
m_a_p = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}\n")
position = input("Where do you want to put the treasure:?")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = m_a_p[vertical - 1]
selected_row[horizontal - 1] = "x"
print(f"{row_1}\n{row_2}\n{row_3}\n")


