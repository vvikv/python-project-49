from brain_games.games.game_parity_check import parity_check, number_game_even
from brain_games.games.game_calc import game_calc
from brain_games.logic.logic_components import end_game
from brain_games.logic.logic_components import get_user_answer, print_correct
from brain_games.logic.greetings import name
from brain_games.games.game_gcd import game_gcd
from brain_games.games.game_progression import game_progression
from brain_games.games.game_prime import game_prime


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


def game_logic_calc():
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        correct_answer, question = game_calc()
        print('Question: ' + question)
        answer = get_user_answer()
        count += 1
        print_correct(answer, correct_answer)
        end_game(count, answer, correct_answer, name)


def game_logic_gcd():
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        correct_answer, question = game_gcd()
        print('Question: ' + question)
        answer = get_user_answer()
        count += 1
        print_correct(answer, correct_answer)
        end_game(count, answer, correct_answer, name)


def game_logic_progression():
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        correct_answer, question = game_progression()
        print('Question: ' + question)
        answer = get_user_answer()
        count += 1
        print_correct(answer, correct_answer)
        end_game(count, answer, correct_answer, name)


def game_logic_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        correct_answer, question = game_prime()
        print('Question: ' + question)
        answer = get_user_answer()
        count += 1
        print_correct(answer, correct_answer)
        end_game(count, answer, correct_answer, name)
