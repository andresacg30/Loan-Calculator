import math
import argparse

# Adding arguments for the command line
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()

# Assigning inputs from the command line to variables
loan_type = args.type
principal = args.principal
monthly_payment = args.payment
periods = args.periods
interest = args.interest
nominal_interest = 0
last_payment = 0

# List for possible errors to the user
total_args = [loan_type, principal, monthly_payment, periods, interest]
numeric_args = [principal, monthly_payment, periods, interest]

# Let's see what we need to calculate
if len([arg for arg in total_args if arg is not None]) < 4:  # Error if there are fewer than 4 parameters are provided
    print("Incorrect parameters")
elif interest is None:  # The calculator can't calculate interest, it must be provided
    print("Incorrect parameters")
elif len([float(arg) for arg in numeric_args if arg is not None and float(arg) < 0])\
        > 0:  # Error if there is a negative number
    print("Incorrect parameters")
else:
    if loan_type == "annuity":  # Calculations for annuity payments
        if periods is None:  # Calculate the full time to repay the loan
            monthly_payment = float(monthly_payment)
            principal = float(principal)
            interest = float(interest)
            nominal_interest = (interest / 1000) / (12 * 0.100)
            x = monthly_payment / (monthly_payment - nominal_interest * principal)
            periods = math.ceil(
                math.log(x, 1 + nominal_interest)
            )
            years, month = periods // 12, periods % 12
            if monthly_payment == principal:
                print(f"It will take {periods} month to repay the loan!")
            elif years == 0:
                print(f"It will take {month} months to repay the loan!")
            elif month == 0:
                print(f"It will take {years} years to repay the loan!")
            else:
                print(f"It will take {years} years and {month} months to repay the loan!")
            overpayment = (monthly_payment * periods) - principal
            print(f"Overpayment = {math.ceil(overpayment)}")
        elif monthly_payment is None:  # Calculate the monthly payment and the overpayment
            principal = float(principal)
            periods = int(args.periods)
            interest = float(interest)
            nominal_interest = (interest / 1000) / (12 * 0.100)
            monthly_payment = math.ceil(principal * (nominal_interest * (math.pow(1 + nominal_interest, periods) /
                                                                         (math.pow(1 + nominal_interest, periods)
                                                                          - 1))))
            overpayment = (monthly_payment * periods) - principal
            print(f"Your annuity payment = {monthly_payment}!")
            print(f"Overpayment = {math.ceil(overpayment)}")
        elif principal is None:  # Calculate the total payment and the overpayment
            monthly_payment = float(monthly_payment)
            periods = int(args.periods)
            interest = float(interest)
            nominal_interest = (interest / 1000) / (12 * 0.100)
            principal = math.floor(monthly_payment / (nominal_interest * (math.pow(1 + nominal_interest, periods)
                                                                          / (math.pow(1 + nominal_interest,
                                                                                      periods) - 1))))
            print(f"Your loan principal = {principal}!")
            overpayment = (monthly_payment * periods) - principal
            print(f"Overpayment = {math.ceil(overpayment)}")
        else:
            print("Incorrect parameters")
    elif loan_type == "diff":  # Calculations for differentiated payments
        if monthly_payment is not None:
            print("Incorrect parameters")
        elif monthly_payment is None:
            principal = float(principal)
            periods = int(args.periods)
            interest = float(interest)
            nominal_interest = (interest / 1000) / (12 * 0.100)
            months = 0
            for month in range(1, periods + 1):
                payment = math.ceil(
                    (principal / periods) + nominal_interest * (principal - (principal * (month - 1) / periods))
                )
                months += payment
                print(f"Month {month}: payment is {payment}")
            overpayment = months - principal
            print()
            print(f"Overpayment = {math.ceil(overpayment)}")
        else:
            print("Incorrect parameters")
