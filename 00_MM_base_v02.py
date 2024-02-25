# functions go here

# checks user has entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")

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


# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = yes_no("do you want to read the Instructions? ")

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
    print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost))

    tickets_sold += 1

# output number of tickets sold
    if tickets_sold == MAX_TICKETS:
        print("Congratulations you have sold all the tickets")
    else:
        print("you have sold {} ticket/s. there is {} ticket/s "
              "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))