# ************************************************************
# *                                                          *
# * CSCE 3390            Spring 2023         Gabriel Torres  *
# *                                                          *
# *                       Homework 1                         *
# *                                                          *
# *                  Date Created: 01/23/2023                *
# ************************************************************

print("*****************************************\n"
      "*  Weekly Payroll Calculation Software  *\n"
      "*****************************************")

REGULAR_PAY_RATE = 59.78
OVERTIME_PREMIUM = 1.50
decision = 'y'
while decision == 'y' or decision == 'Y':
    employee_SSN = input("\nEnter employee SSN (digits only, no spaces or dashes: ")
    hours_worked = float(input("Enter hours worked: "))
    num_of_dependents = int(input("Enter number of dependents: "))

    print("\nWeekly Payment Report:")
    print("=========================================")
    print("Social Security Number: " + employee_SSN)
    print("Hours worked: " + str("%.2f" % hours_worked))
    print("Regular pay rate: $" + str(REGULAR_PAY_RATE))
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        print("Overtime hours worked: " + str("%.2f" % overtime_hours))
        print("With overtime premium: " + str("%.2f" % OVERTIME_PREMIUM))
        weekly_gross_pay = REGULAR_PAY_RATE * 40 + (OVERTIME_PREMIUM * REGULAR_PAY_RATE * overtime_hours)
    else:
        weekly_gross_pay = REGULAR_PAY_RATE * hours_worked

    social_security_tax = weekly_gross_pay * .06
    federal_income_tax = weekly_gross_pay * .14
    state_income_tax = weekly_gross_pay * .05
    union_dues = 10.00
    print("Your weekly gross pay: $" + str("%.2f" % weekly_gross_pay))
    print("Social Security Tax: $" + str("%.2f" % social_security_tax))
    print("Federal Income Tax: $" + str("%.2f" % federal_income_tax))
    print("State Tax: $" + str("%.2f" % state_income_tax))

    # Check number of depends, if 3 or greater, add health insurance
    if num_of_dependents > 2:
        health_insurance = 35
        print("Health Insurance amount: $" + str("%.2f" % health_insurance))
    else:
        health_insurance = 0

    print("Union Dues amount: $" + str("%.2f" % union_dues))

    # calculate take home pay
    take_home_pay = weekly_gross_pay - (social_security_tax + federal_income_tax + state_income_tax + union_dues + health_insurance)
    print("Net Take-Home Pay of the week: $" + str("%.2f" % take_home_pay))
    print("=========================================")
    print("Compute pay for another employee?")

    # Ask user to repeat program
    decision = input("Y / y repeats, any other ends: ")

