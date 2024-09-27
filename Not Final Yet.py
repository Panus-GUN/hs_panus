def intro(): -> None
    # Greet user 
    print("Hi there, welcome! What's your name, buddy?")
    name = input("Enter your name: ")
    
    # introduction 
    print(f"\nNice to meet you, {name}! I'm here to help guide you through the world of investment,
           and to show you how important it is for your future.")
    
    # monthly saving
    monthly_saving = float(input("\nHow much can you save each month, or do you have a number in mind? Enter your monthly savings: "))
    
    # Example of potential investment growth after 20 years
    print(f"\nGreat! You're saving {monthly_saving:.2f} per month—awesome start! Here's an example of what could happen to your money if you invest it in different places over 20 years.\n")
    
    # Display future value examples for different investments
    show_investment_scenarios(monthly_saving)

def show_investment_scenarios(monthly_saving: float) -> None:
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
    
    print(f"Why 20 years? Because after 20 years,
           the risk almost disappears and your investments can grow!\n")
    
    # Show the calculated future values
    print(f"Bank Savings (1% interest): ${bank_value:.2f}")
    print(f"Mutual Funds (5% interest): ${fund_value:.2f}")
    print(f"Stocks (8% interest): ${stocks_value:.2f}")
    print(f"Cryptocurrency (12% interest): ${crypto_value:.2f}")
    
    print("\n**Remember:**")
    print("The higher the potential return,/the higher the risk. But with the right knowledge, you can turn 'risk' into opportunity!")

    input("\nTap to continue...")

    # Continue guiding the user to their personal investment plan
    personal_plan()

def personal_plan():
    # Guide the user through their personal plan
    print("\nNow it's your turn! Let's build a plan together.")
    
    # Recommend risk profile based on user’s age and income
    age = int(input("How old are you? "))
    income = float(input("What's your annual income? "))
    
    # Determine the risk profile based on user’s age and income
    risk_profile = assess_risk_profile(age, income)
    print(f"\nYour recommended risk level is: {risk_profile}.")
    
    # Get user’s goal
    goal = input("What’s your plan? Are you saving for a house, a vacation, retirement? ")
    
    # Get the time frame to reach the goal
    years_until_goal = int(input("How many years until you want to achieve this goal? "))
    
    # Confirm monthly savings
    monthly_saving = float(input("Confirm your monthly savings: "))
    
    # Display final investment recommendation based on risk profile
    recommend_investment(monthly_saving, risk_profile, years_until_goal)

def assess_risk_profile(age, income):
    # Simple logic to assess the risk profile based on age and income
    if age < 30 and income > 50000:
        return "High Risk"
    elif age < 45 and income >= 30000:
        return "Medium Risk"
    else:
        return "Low Risk"

def recommend_investment(monthly_saving, risk_profile, years):
    # Recommend an investment strategy based on the user's risk profile
    if risk_profile == "High Risk":
        expected_return = 0.10
    elif risk_profile == "Medium Risk":
        expected_return = 0.06
    else:
        expected_return = 0.03
    
    future_investment_value = future_value(monthly_saving, expected_return, years)
    
    print(f"\nBased on your goal, your monthly savings,
           and your risk profile ({risk_profile}), you should aim for assets generating approximately {expected_return*100}% return.")
    print(f"If you save {monthly_saving:.2f} per month for {years} years, you could accumulate around ${future_investment_value:.2f}.\n")

def future_value(monthly_saving, annual_rate, years):
    # Calculate future value using compound interest formula for regular monthly contributions
    months = years * 12
    monthly_rate = annual_rate / 12
    future_value = monthly_saving * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    return future_value

# Run the intro to start the program
intro() 