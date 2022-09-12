import prompt as prompt
from random import randint
from brain_games.greetings import name
from random import randint, choice
from math import sqrt

print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    if n > 1:
        return True


def game_prime():
    count = 0

    while count < 3:
        a = randint(1, 200)
        question = str(a)
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if is_prime(a) and answer == 'yes':
            print('Correct!')
        elif is_prime(a) == False and answer == 'yes':
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
        elif is_prime(a) == False and answer == 'no':
            print('Correct!')
        elif is_prime(a) and answer == 'no':
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
        count += 1
    print(f'Congratulations, {name}!')