def weekly_to_monthly(weekly_wage):
    
    annual_salary = weekly_wage * 52
    monthly_salary = annual_salary / 12
    return monthly_salary
try:
    user_wage = float(input("Enter your weekly wage: "))
    result = weekly_to_monthly(user_wage)
    print(f"Your estimated monthly salary in rupees:{result:.2f}")

except ValueError:
    print("Please enter a valid numeric value.")
