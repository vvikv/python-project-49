import prompt as prompt
from random import randint

print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print('Hello, ' + name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def answer_user():
    count = 0

    while count < 3:
        number = randint(1, 1000)
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

