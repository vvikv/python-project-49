import prompt as prompt
from random import randint
from brain_games.greetings import name

print('Find the greatest common divisor of given numbers.')


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def game_gcd():
    count = 0

    while count < 3:
        a = randint(1, 100)
        b = randint(1, 100)
        question = str(a) + ' ' + str(b)
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        correct_answer = gcd(a, b)
        if answer == str(correct_answer):
            print('Correct!')
        elif answer != str(correct_answer):
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
        count += 1
    print(f'Congratulations, {name}!')
