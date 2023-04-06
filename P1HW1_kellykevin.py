# Travel expense project
# 4/5/2023
# CTI-110 P1HW1 - Travel Expense
# Kelly, Kevin
#

print('This program calculates and displays travel expenses')
print()
budg1 = int(input("Enter budget:  "))
print()
dest1 = input("Enter your travel destination:  ")
print()
gas1 = int(input("How much do you think you will spend on gas?  "))
print()
stay1 = int(input("Approximately, how much will you need for accomdation/hotel?  "))
print()
food1 = int(input("Last, how much do you need for food?  "))
print()
#we will get the remaining balance by subtracting fuel, hotel costs, and food from the budget
rem1 = budg1 - gas1 - stay1 - food1
print("------------Travel Expenses------------")
print()
print("Location: ", dest1)
print("Initial Budget: ",budg1)
print()
print("Fuel: ",gas1)
print("Accomodations: ",stay1)
print("Food: ",food1)
print()
print("Remaining Balance: ",rem1)
