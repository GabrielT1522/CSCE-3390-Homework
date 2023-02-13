# ************************************************************
# *                                                          *
# * CSCE 3390            Spring 2023         Gabriel Torres  *
# *                                                          *
# *                       Homework 1                         *
# *                                                          *
# *                  Date Created: 01/20/2023                *
# ************************************************************

# Input
miles_driven_per_day = float(input("Enter miles driven per day: "))
cost_per_gallon = int(input("Enter cost per gallon of gas (in cents): "))
avg_miles_per_gallon = float(input("Enter average miles per gallon: "))
parking_fees_per_day = float(input("Enter parking fees per day (in dollars): "))
tolls_per_day = float(input("Enter tolls per day (in dollars): "))

# Calculate daily driving cost
daily_driving_cost = (miles_driven_per_day / avg_miles_per_gallon) * (cost_per_gallon * .01) + (parking_fees_per_day + tolls_per_day)

# Output
print("Your daily driving cost is: $"+str(daily_driving_cost))



