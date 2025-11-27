# Home loan calculator 
# This program calculates the interest and total amount to be paid on a users personal loan
# based on user input for interest type (simple or compound).

principal = 1000000
annual_interest_rate = 7/ 100  # Convert 7% to decimal
loan_tenure_years = 10
compounding_periods =1 # annual compounding

interest_type = input("Enter interest type (simple or compound): ").lower()

is_valid = True
if interest_type == "simple":
    # Simple Interest Calculation
    simple_interest = (principal * annual_interest_rate * loan_tenure_years)
    total_amount = principal + simple_interest
    print(f"Simple Interest: {simple_interest:.2f}")
    print(f"Total Amount to be paid: {total_amount:.2f}")

elif interest_type == "compound":
    # Compound Interest Calculation
    n = compounding_periods
    r = annual_interest_rate
    t = loan_tenure_years
    compound_interest = principal * (1 + r / n) ** (n * t) - principal
    total_amount = principal + compound_interest
    print(f"Compound Interest: {compound_interest:.2f}")
    print(f"Total Amount to be paid: {total_amount:.2f}")
    
else:
    is_valid = False
if not is_valid:
    print("Invalid interest type entered. Please enter 'simple' or 'compound'.")