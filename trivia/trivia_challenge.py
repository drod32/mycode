#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random

URL= "https://opentdb.com/api.php?amount=10&difficulty=medium"

def start_game():
    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()
    return data

def check_answer(correct, user_answer):
    if correct.lower().strip() == user_answer.lower().strip():
        print("Good Job!!!")
    else:
        print("Better luck next time!")

def answer_bank(trivia):
    answer_bank = []
    print(trivia["question"])
    answer_bank.append(trivia["correct_answer"])
    for wrong_answer in trivia["incorrect_answers"]:
        answer_bank.append(wrong_answer)
    random.shuffle(answer_bank)
    for answer in answer_bank:
        print(answer)

def main():
    
    data = start_game()
    
    for trivia in data["results"]:        
        answer_bank(trivia)
        correct = trivia["correct_answer"]
        user_answer = input("choose the correct answer.\n>>")
        check_answer(correct, user_answer)        
        continue_game = input("press enter to continue")
        
if __name__ == "__main__":
    main()

