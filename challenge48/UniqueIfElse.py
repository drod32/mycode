#!/usr/bin/python3

def main():

    attempts = 0
    points = 0
    question1 = "This 2000s hit features a popular rapper asking his partner 21 questions, who is that rapper?"
    bonus1 = "For a chance to win the game, What year was this song released"
    while True:
        if points == 10:
            print("congrats you win")
            break
        elif attempts == 3:
            print("sorry you lose")
            break
        else: 
            print(question1)
            answer1 = input("Your answer >>> ")
            if answer1 == "50" or answer1.lower() == "50 cent":
                points = points + 5
                print(f"good Job, you have {points} points\n")
                print(bonus1)
                try:
                    bonus_answer = int(input("Your answer >>> "))
                    if bonus_answer == 2003:
                        points = points + 5
                        print(f"congrats you have {points} points\n")
                    else:
                        print("sorry 2003 is the correct year\n")
                except ValueError as err:
                    print("sorry you entered an invalid value\n")
            else:
                attempts = attempts + 1
                print("sorry that answer is incorrect use google to find the correct answer\n")
main()
