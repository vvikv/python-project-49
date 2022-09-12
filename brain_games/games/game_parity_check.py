import prompt as prompt
from brain_games.greetings import name
from random import randint

print('Answer "yes" if the number is even, otherwise answer "no".')


def parity_check():
    count = 0

    while count < 3:
        number = randint(1, 100)
        question = ('Question: ' + str(number))
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and number % 2 == 0 or answer == 'no' and number % 2 > 0:
            print('Correct!')
        elif answer == 'yes' and number % 2 > 0:
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
        elif answer == 'no' and number % 2 == 0:
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
        elif answer != 'no' and answer != 'yes' and number % 2 == 0:
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
        elif answer != 'no' and answer != 'yes' and number % 2 > 0:
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
        count += 1
    print(f'Congratulations, {name}!')

