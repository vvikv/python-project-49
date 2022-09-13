from brain_games.logic.random_numbers import create_random_number
from random import choice


def random_operation():
    lst = ['+', '*', '-']
    operation = choice(lst)
    return operation


def game_calc():
    num1 = create_random_number()
    num2 = create_random_number()
    operation = random_operation()
    question = str(num1) + ' ' + operation + ' ' + str(num2)
    correct_answer = eval(question)
    return correct_answer, question
