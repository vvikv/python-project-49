from math import sqrt
from brain_games.logic.random_numbers import create_random_number


def is_prime(num):
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    if num > 1:
        return True


def game_prime():
    num = create_random_number()
    question = str(num)
    if is_prime(num) is True:
        correct_answer = 'yes'
    elif is_prime(num) is False:
        correct_answer = 'no'
    return correct_answer, question
