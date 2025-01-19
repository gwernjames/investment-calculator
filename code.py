def investment_calculator():

    # Input data
    principal = float(input("Initial investment amount (principal): "))
    monthly_contribution = float(input("Monthly contribution amount: "))
    annual_rate = float(input("Annual interest rate (S&P500 Average 10%): ")) / 100
    years = int(input("Enter the number of years: "))

    monthly_interest_rate = annual_rate / 12
    number_months = years * 12

    # Formula explain
    # FV = P(1+r)^n + C x ((1+r)^n - 1) / r
    # FV = Future Value
    # P = Principle
    # C = contributions
    # r = Monthly interest rate (annual interest rate divided by 12).
    # n = number of months (years * 12)

    # Calculations
    future_value_work = principal * (1 + monthly_interest_rate)**number_months
    contribution_work = monthly_contribution * (((1 + monthly_interest_rate)**number_months) - 1) / monthly_interest_rate
    future_value = future_value_work + contribution_work

    # Output
    print("\nInvestment Calculator:")
    print(f"Principal Amount: £{principal:,.2f}")
    print(f"Annual Interest Rate: {annual_rate * 100:.2f}%")
    print(f"Time Period: {years} years")
    print(f"Future Value of Investment: £{future_value:,.2f}")


investment_calculator()
