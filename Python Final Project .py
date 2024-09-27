def intro() -> None:
    # Greet user
    print("Hi there, welcome! What's your name, buddy?")
    name = input("Enter your name: ")

    # Introduction message
    print(f"\nNice to meet you, {name}! I'm here to help guide you through the world of investment, "
          "and to show you how important it is for your future.")

    # Validate monthly saving input
    while True:
        try:
            monthly_saving = float(input("\nHow much can you save each month, or do you have a number in mind? "
                                         "Enter your monthly savings: "))
            if monthly_saving < 0:
                print("Please enter a valid number for monthly savings (greater than or equal to 0).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value for monthly savings.")

    # Example of potential investment growth after 20 years
    print(f"\nGreat! You're saving {monthly_saving:,.0f} per month—awesome start! Here's an example of what "
          "could happen to your money if you invest it in different places over 20 years.\n")

    # Display future value examples for different investments
    show_investment_scenarios(monthly_saving)

def show_investment_scenarios(monthly_saving: float) -> None:
    """
    Display all possible scenarios according to the user's monthly saving.
    """
    # Define sample interest rates for different investment types
    bank_rate = 0.01
    fund_rate = 0.05
    stocks_rate = 0.10
    crypto_rate = 0.20

    years = 30
    # Calculate future value based on monthly savings and rates
    bank_value = future_value(monthly_saving, bank_rate, years)
    fund_value = future_value(monthly_saving, fund_rate, years)
    stocks_value = future_value(monthly_saving, stocks_rate, years)
    crypto_value = future_value(monthly_saving, crypto_rate, years)

    print(f"Why 20 years? Because after 20 years, the risk almost disappears and your investments can grow!\n")

    # Show the calculated future values with comma and no decimal places
    print(f"Bank Savings (1% interest): ${bank_value:,.0f}")
    print(f"Mutual Funds (5% interest): ${fund_value:,.0f}")
    print(f"Stocks (10% interest): ${stocks_value:,.0f}")
    print(f"Cryptocurrency (20% interest): ${crypto_value:,.0f}")

    print("\n**Remember:**")
    print("The higher the potential return, the higher the risk. But with the right knowledge, "
          "you can turn 'risk' into opportunity!")

    input("\nTap to continue...")

    # Continue guiding the user to their personal investment plan
    personal_plan()

def personal_plan() -> None:
    # Guide the user through their personal plan
    print("\nNow it's your turn! Let's build a plan together.")

    # Validate age input
    while True:
        try:
            age = int(input("How old are you? "))
            if age < 0:
                print("Please enter a valid age (greater than or equal to 0).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value for age.")

    # Validate income input
    while True:
        try:
            income = float(input("What's your annual income? "))
            if income < 0:
                print("Please enter a valid number for annual income (greater than or equal to 0).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value for annual income.")

    # Determine the risk profile based on user’s age and income
    risk_profile = assess_risk_profile(age, income)
    print(f"\nYour recommended risk level is: {risk_profile}.")

    # Get user’s goal
    goal = input("What’s your plan? Are you saving for a house, a vacation, retirement? ")

    # Validate years until goal input
    while True:
        try:
            years_until_goal = int(input("How many years until you want to achieve this goal? "))
            if years_until_goal < 0:
                print("Please enter a valid number of years (greater than or equal to 0).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value for years.")

    # Validate monthly savings confirmation input
    while True:
        try:
            monthly_saving = float(input("Confirm your monthly savings: "))
            if monthly_saving < 0:
                print("Please enter a valid number for monthly savings (greater than or equal to 0).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numerical value for monthly savings.")

    # Display final investment recommendation based on risk profile
    recommend_investment(monthly_saving, risk_profile, years_until_goal)

def assess_risk_profile(age: int, income: float) -> str:
    """
    Assess the risk profile based on age and income.
    """
    if age <= 20:
        print("\nSince you're young and have a long time for compound interest to work, "
              "a high-risk investment is a great option for you.")
        return "High Risk"
    elif 21 <= age <= 30:
        if income >= 20000:
            return "High Risk"
        else:
            return "Medium Risk"
    elif 31 <= age <= 50:
        if income > 80000:
            return "High Risk"
        elif income > 30000:
            return "Medium Risk"
        else:
            return "Low Risk"
    else:
        print("\nDue to your age, a low-risk investment is more suitable to ensure safety in the long run.")
        return "Low Risk"

def recommend_investment(monthly_saving: float, risk_profile: str, years: int) -> None:
    """
    Recommend an investment strategy based on the user's risk profile.
    """
    if risk_profile == "High Risk":
        expected_return = 0.10
    elif risk_profile == "Medium Risk":
        expected_return = 0.06
    else:
        expected_return = 0.03

    future_investment_value = future_value(monthly_saving, expected_return, years)

    print(f"\nBased on your goal, your monthly savings, and your risk profile ({risk_profile}), "
          f"you should aim for assets generating approximately {expected_return*100}% return.")
    print(f"If you save {monthly_saving:,.0f} per month for {years} years, "
          f"you could accumulate around ${future_investment_value:,.0f}.\n")

def future_value(monthly_saving: float, annual_rate: float, years: int) -> float:
    """
    Calculate future value using compound interest formula for regular monthly contributions.
    """
    months = years * 12
    monthly_rate = annual_rate / 12
    future_value = monthly_saving * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    return future_value

# Run the intro to start the program
intro()

