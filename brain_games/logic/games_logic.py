from brain_games.logic.greetings import name
import prompt as prompt
from random import randint
from brain_games.games.game_parity_check import parity_check, number_game_even
import sys


def get_user_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def end_game_text(answer, correct_answer, name):
    text_one = f"""'{answer}' is wrong answer ;(."""
    text_second = f"""Correct answer was {correct_answer}."""
    text_third = f"""Let's try again, {name}!"""
    full_text = f"""{text_one} {text_second}\n{text_third}"""
    print(full_text)


def print_correct(answer, correct_answer):
    if answer_check(answer, correct_answer) is True:
        print('Correct!')


def game_logic_parity():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = number_game_even()
        print('Question: ' + str(random_number))
        correct_answer = parity_check(random_number)
        answer = get_user_answer()
        count += 1
        print_correct(answer, correct_answer)
        end_game(count, answer, correct_answer, name)


def answer_check(answer, correct_answer):
    if answer == str(correct_answer):
        return True
    elif answer != str(correct_answer):
        return False


def end_game(count, answer, correct_answer, name):
    if answer_check(answer, correct_answer) is False:
        sys.exit(end_game_text(answer, correct_answer, name))
    elif count == 3:
        print(f'Congratulations, {name}!')
