import math

while True:
#Ask user which calculator they want to use
    try:
        calc_choice = input("Which calculator would you like to use? Investment? or Bond? ")
        if calc_choice.isalpha():
            calc_choice  = calc_choice.lower().split()   #Convert input to lowercase, split on whitespace to check for one word input.
        if (calc_choice  == "bond") or (calc_choice  == "investment"):
            print(f"You have chosen to use the {calc_choice[0]} calculator!")
    except ValueError:
        print("Invalid input! Please try again")
        continue

# while True:
#Bond calculator, outputs repayment per month, rounded to 2dp
    if (calc_choice[0] == "bond"):
        try:
            house_value = float(input("Current value of the house? "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        user_interest_rate = float(input("Current annual interest rate %? "))
        monthly_interest_rate = float((user_interest_rate/100)/12)
        n_months = float(input("How many months to repay the bond? "))
        repayment = (monthly_interest_rate * house_value)/(1-(1+monthly_interest_rate)**(-n_months))
        print(f"Your monthly repayment will be {math.ceil(repayment*100)/100}.")
        continue
#Invesment Calculator
    elif (calc_choice[0] == "investment"):
        deposit = float(input("How much money are you depositing? "))
        user_interest_rate = float(input("Interest rate % ? "))
        decimal_int_rate = (user_interest_rate/100)
        n_years = float(input("How many years will you be investing this for? "))
        interest = input("'simple' or 'compound' interest? ")
        interest = interest.lower()

#Simple interest
        if (interest == "simple"):
            inv_value = deposit * (1 + decimal_int_rate*n_years)
            print(f"Your investment will be worth {math.ceil(inv_value*100)/100}")
            continue
#Compound interest
        elif (interest == "compound"):
            inv_value = deposit * math.pow((1+decimal_int_rate),n_years)
            print(f"Your investment will be worth {math.ceil(inv_value*100)/100}")
            continue
        else:
            print("Invalid input, please try again!")
                
    else:
        print("Invalid input. Please run and try again. Bond or Investment?")
        continue
