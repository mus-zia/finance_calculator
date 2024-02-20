
# FINAL ITERATION. LOTS OF ERROR HANDLING. EXTRA PRACTICE
# Includes error handling of division by 0 and end-of-file error.
import math

while True:
  try:
      calc_choice = input("Which calculator would you like to use? Investment? or Bond? ")
      if calc_choice.isalpha():
          calc_choice = calc_choice.lower().split()
      if len(calc_choice) != 1:
          print("Invalid input! Please enter one word only.")
          continue
      if (calc_choice[0] == "bond") or (calc_choice[0] == "investment"):
          print(f"You have chosen to use the {calc_choice[0]} calculator!")
  except EOFError:
      print("Unexpected end of file. Please try again.")
      continue
  except ValueError:
      print("Invalid input! Please try again")
      continue

  if (calc_choice[0] == "bond"):
      try:
          house_value = float(input("Current value of the house? ").strip())
      except ValueError:
          print("Invalid input! Please enter a valid number.")
          continue
      user_interest_rate = float(input("Current annual interest rate %? ").strip())
      monthly_interest_rate = float((user_interest_rate/100)/12)
      n_months = float(input("How many months to repay the bond? ").strip())
      try:
          repayment = (monthly_interest_rate * house_value)/(1-(1+monthly_interest_rate)**(-n_months))
      except ZeroDivisionError:
          print("Invalid input! Division by zero is not allowed.")
          continue
      print(f"Your monthly repayment will be {math.ceil(repayment*100)/100}.")
      continue

  elif (calc_choice[0] == "investment"):
      try:
          deposit = float(input("How much money are you depositing? ").strip())
      except ValueError:
          print("Invalid input! Please enter a valid number.")
          continue
      user_interest_rate = float(input("Interest rate % ? ").strip())
      decimal_int_rate = (user_interest_rate/100)
      n_years = float(input("How many years will you be investing this for? ").strip())
      interest = input("'simple' or 'compound' interest? ").strip().lower()

      if (interest == "simple"):
          try:
              inv_value = deposit * (1 + decimal_int_rate*n_years)
          except ZeroDivisionError:
              print("Invalid input! Division by zero is not allowed.")
              continue
          print(f"Your investment will be worth {math.ceil(inv_value*100)/100}")
          continue
      elif (interest == "compound"):
          try:
              inv_value = deposit * math.pow((1+decimal_int_rate),n_years)
          except ZeroDivisionError:
              print("Invalid input! Division by zero is not allowed.")
              continue
          print(f"Your investment will be worth {math.ceil(inv_value*100)/100}")
          continue
      else:
          print("Invalid input, please try again!")
              
  else:
      print("Invalid input. Please run and try again. Bond or Investment?")
      continue
