# functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("please choose a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("choose a payment method (cash "
                                 " or credit): ")

    print("You choose", payment_method)

    print()





