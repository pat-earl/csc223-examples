print("Enter number of hours worked:")
hours = int(input())
wage = int(input("Enter your hourly rate:"))

if hours < 0 or wage < 0:
    print("You can't work less than 0 hours!")


else:
    pay = hours * wage
    print("Payment Amount: $" + str(pay))