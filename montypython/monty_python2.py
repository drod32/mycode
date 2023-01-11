#!/usr/bin/env python3

round = 0

#begins Loop
while True:

    # round counter
    round = round + 1

    #ask user for name of movie trivia
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______"\nYour guess--> ')

    # if user answers correctly they win
    if answer.title() == "Brian":
        print("Correct!")
        break

    elif answer.lower() == "shrubbery":
        print("You gave the super secret answer!")
        break

    # if user fails 3 times they lose
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break

    # allows the user to attemp again
    else:
        print("try again")

