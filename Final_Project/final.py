# Final Game
# This game is a set of trivia questions related to historical events

import random

# This function imports the trivia questions from a text file
def import_questions(file_path):
    with open(file_path, "r") as file:
            lines= file.readlines()
            questions = [line.strip() for line in lines if line.strip()]
    return questions

# This function randomly selects an trivia question for the player

def quiz_and_answer(questions):
    #splits the question and anwser by the question mark
    random_question = random.choice(questions).split("? ")
    question = random_question[0] 
    answer = random_question[1] 
    return question, answer

# asks the questions

def ask_question(questions):
    question, answer = quiz_and_answer(questions)
    return question, answer

questions = import_questions("/users/sophiadow/Desktop/CSCI_110/scripts/questions.txt")

print("Welcome to Historic Trivia! Answer the questions right to win!")
score = 0
while True:
    input("Press Enter to see a question")
    question, answer = ask_question(questions)
    print("Question:", question)
    player_answer = input("Answer: ").strip().lower()

    if player_answer == answer.lower():
        print("Good job history buff!")
        score +=1
    else:
        print("WRONG. The correct answer is:", answer)

    print("Your score is:", score)

# This game is very finicky you have to put the exact right answer as was inputed in the txt file or you get it wrong






# Testing
#This was the only function I could figure out testing on :(
import unittest

class test_game(unittest.TestCase):
    def test_quiz_and_answer(self):
        questions = ["The United States bought Alaska from which country? Russia", "Who was the fourth president of the United States? James Madison"]
        question, answer = quiz_and_answer(questions)
        

# Thank you to python.org for teaching unittest
