from brain_games.logic.random_numbers import create_random_number


def number_game_even():
    random_number = create_random_number()
    return random_number


def parity_check(random_number):
    if random_number % 2 == 0:
        correct_answer = 'yes'
    elif random_number % 2 > 0:
        correct_answer = 'no'
    return correct_answer
