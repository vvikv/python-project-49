import prompt as prompt
import sys


def get_user_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def end_game_text(answer, correct_answer, name):
    text_one = f"""'{answer}' is wrong answer ;(."""
    text_second = f"""Correct answer was '{correct_answer}'."""
    text_third = f"""Let's try again, {name}!"""
    print(f"""{text_one} {text_second}\n{text_third}""")


def print_correct(answer, correct_answer):
    if answer_check(answer, correct_answer) is True:
        print('Correct!')


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
