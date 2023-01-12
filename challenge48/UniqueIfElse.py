#!/usr/bin/python3

import random

def main():

    attempts = 0
    points = 0
    questions = ["This 2000s hit features a popular rapper asking his partner 21 questions, who is that rapper?", "Finish these Yung Joc lyrics: Meet me in the mall, __________ Meet me in the club, __________."]
    bonus = "For bonus points, What year was this song released"
    answers = ["50 cent", "its goin down"]
    bonus_answers = [2003, 2006]
    while True:
        question_number = random.randrange(0,2)
        if points >= 4:
            print("congrats you win")
            break
        elif attempts == 3:
            print("sorry you lose")
            break
        else:
            print(f"attempts remaining: {3 - attempts}")
            print(questions[question_number])
            user_answer = input("Your answer >>> ")
            if user_answer.strip().lower().replace("'","") == answers[question_number]:
                points = points + 2
                print(f"good Job, you have {points} points\n")
                print(bonus)
                try:
                    bonus_input = int(input("Your answer >>> "))
                    if bonus_input == bonus_answers[question_number]:
                        points = points + 2
                        print(f"congrats you have {points} points\n")
                    else:
                        print(f"sorry {bonus_input} is incorrect\n")
                except ValueError as err:
                    print("sorry you entered an invalid value\n")
            else:
                attempts = attempts + 1
                print("sorry that answer is incorrect use google to find the correct answer\n")

if __name__ == "__main__":
    main()
