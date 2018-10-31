monthly_salary = int(input("Enter your annual salary: ")) / 12
# annual_salary = int("Enter your annual salary: ")
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
# total_cost = int(total_cost)
# print(total_cost)
portion_down_payment = float(0.25 * total_cost)
# print(portion_down_payment)
current_savings = int(0)
r = float(0.04)
annual_return = current_savings * r/12
# print(annual_return)
months = int(0)


# (current_savings * 0.04)/12)
while (current_savings <= portion_down_payment):
    #calculate interest
    interest = float(current_savings * 0.04)/12
    #add portion_saved
    monthly_saved = portion_saved * monthly_salary
    #add interest + portion_saved + current savings
    current_savings = interest + monthly_saved + current_savings

    months = months + 1
# print when months stop increasing by 1/print months when conditions are met--stuck here!!
# If (months = )

print("Enter your annual salary: " + str(monthly_salary * 12))   
print("Enter the percent of your salary to save, as a decimal: " + str(portion_saved))
print("Enter the cost of your dream home: " + str(total_cost))
print("Number of months: " + str(months))

