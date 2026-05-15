#Ex2C 

#Lab 2 : more functions 

#Defining and displaying mailing label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")

#Testing the mailing label 
display_mailing_label(
    "Smaya Melgara",
    "123 Main Street",
    "Charlotte",
    "NC",
    "28202"
)

#Adding an unlimited amount of numbers 
def add_numbers(*numbers):
    total = sum(numbers)
    expression = " + ".join(str(num) for num in numbers)
    print(f"{expression} = {total}")

#Testing the number code
add_numbers(8)
add_numbers(3,20)
add_numbers(1,2,3,4,5)

#Receipt Function
def display_receipt(total_due, amount_paid):

    change_due = amount_paid - total_due

    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due:
        print(f"Change Due: ${change_due}")

    elif amount_paid == total_due:
        print("Change Due: $0")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")
        
#Test Receipt code 
display_receipt(23,60)
display_receipt(43,43)
display_receipt(52,30)

#BONUS: ADDRESS ALLOWING MORE LINES IN THE ADDRESS LINE 
def display_mailing_label2(
    name,
    address1,
    city,
    state,
    zip,
    address2=""
):

    print(name)
    print(address1)

    if address2 != "":
        print(address2)

    print(f"{city}, {state} {zip}")
    
#Bonus Test 
display_mailing_label2(
    "Smaya Melgara",
    "123 Main Street",
    "Charlotte",
    "NC",
    "28202"
) 

#BONUS: Receipt where there is multiple totals to be inserted 
def display_receipt2(amount_paid, *totals):

    total_due = sum(totals)

    change_due = amount_paid - total_due

    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due:
        print(f"Change Due: ${change_due}")

    elif amount_paid == total_due:
        print("Change Due: $0")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

#Test Bonus Receipt 
display_receipt2(100,25,30,15)


