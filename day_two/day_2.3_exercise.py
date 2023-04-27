"""Your life in weeks, days and months"""
user_life_span = 90
user_current_age = input("What is your current age?: ")
user_age_as_int = int(user_current_age)
user_months_remaining = (user_life_span * 12) - (user_age_as_int * 12)
user_weeks_remaining = (user_life_span * 52) - (user_age_as_int * 52)
user_days_remaining = (user_life_span * 365) - (user_age_as_int *365)

print(f"You have {user_days_remaining} days, {user_weeks_remaining} weeks, {user_months_remaining} months left.")

