"""
This is a BMI calculator

Don't change the code below!
"""

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_as_float = float(height)
weight_as_int = int(weight)

B_M_I = weight_as_int / (height_as_float**2)
print(int(B_M_I))


