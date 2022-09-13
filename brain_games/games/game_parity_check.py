import prompt as prompt
from brain_games.logic.greetings import name
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

# def u():
#     count = 0
#
#     while count < 3:
#         number = randint(1, 100)
#         question = ('Question: ' + str(number))
#         print(question)
#         answer = prompt.string('Your answer: ')
#         if answer == 'yes' and number % 2 == 0 or answer == 'no' and number % 2 > 0:
#             print('Correct!')
#         elif answer == 'yes' and number % 2 > 0:
#             return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
# Let's try again, {name}!""")
#         elif answer == 'no' and number % 2 == 0:
#             return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
# Let's try again, {name}!""")
#         elif answer != 'no' and answer != 'yes' and number % 2 == 0:
#             return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
# Let's try again, {name}!""")
#         elif answer != 'no' and answer != 'yes' and number % 2 > 0:
#             return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
# Let's try again, {name}!""")
#         count += 1
#     print(f'Congratulations, {name}!')
