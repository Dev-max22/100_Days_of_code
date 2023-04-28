"""
This is a BMI calculator

Don't change the code below!
"""

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height_as_float = float(height)
weight_as_int = int(weight)

B_M_I = weight_as_int / (height_as_float**2)
B_M_I_rounded = round(B_M_I)
if B_M_I < 18.5:
    print(f"Your BMI is {B_M_I_rounded}, You are under-weight")
elif B_M_I <= 25:
    print(f"Your BMI is {B_M_I_rounded},You have a normal weight")
elif B_M_I <= 30:
    print(f"Your BMI is {B_M_I_rounded},You are slightly over-weight")
elif B_M_I <= 35:
    print(f"Your BMI is {B_M_I_rounded},You are obese")
else:
    print(f"Your BMI is {B_M_I_rounded},You are clinically obese")

