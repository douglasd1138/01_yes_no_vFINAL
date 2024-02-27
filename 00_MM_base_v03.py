# functions go here

# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("sorry this cannot be blank. please try again")
        else:
            return response

# checks users enter an integer to a given question
def num_checker(question):
    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print("please enter an integer.")
# main routine goes here

# calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is 7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is 10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket is 6.5 for seniors (65+)
    else:
        price = 6.5

    return price

# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "please chose {} or {}".format(valid_responses[0],
                                           valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
        print(error)



# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Ask user if they want to see the instructions
want_instructions = string_checker("do you want to read the "
                                       "instructions (y/n): ",
                                       1, yes_no_list)

if want_instructions == "yes":
    print("Instructions go here")


# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("please enter your name (or 'XXX' to quit) ")

    if name == 'xxx':
        break

    age = num_checker("Age: ")

    # check user is between 12 and 120 (inclusive)
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? that looks like a typo, please try again.")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("choose a payment "
                                "method (cash / credit): ",
                                2, payment_list)


    tickets_sold += 1

# output number of tickets sold
    if tickets_sold == MAX_TICKETS:
        print("Congratulations you have sold all the tickets")
    else:
        print("you have sold {} ticket/s. there is {} ticket/s "
              "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))