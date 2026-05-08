#Exercise 4C Savings goal
#Lab 2 

bank_balance = 100
savings_goal = 500
weekly_savings = 50

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings

    if bank_balance >= savings_goal:
        print("Goal met! My current balance is $" + format(bank_balance, ".2f"))

    elif bank_balance >= savings_goal * 0.75:
        treat = 10
        bank_balance = bank_balance - treat
        print("So close! After treating myself, my balance is up to $" + format(bank_balance, ".2f"))

    elif bank_balance > savings_goal / 2:
        print("Almost there! This week my balance is up to $" + format(bank_balance, ".2f"))

    else:
        print("This week my balance increased to $" + format(bank_balance, ".2f"))

        