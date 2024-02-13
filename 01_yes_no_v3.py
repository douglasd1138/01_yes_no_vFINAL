# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

     if response == "yes" or response =="y"
         return "yes"

     elif response == "no" or response =="n"
         return "no"

else:
print("please enter yes or no")

# main routine goes here


want_instructions = yes_no("do you want to read the "
                      "instructions? ").lower()

if want_instructions == "yes" or want_instructions == "y":
     print("Instructions go here")
elif want_instructions == "no" or want_instructions == "n":
     pass
else:
     print('please answer yes / no')

print("we are done")





