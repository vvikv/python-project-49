import prompt as prompt
from random import randint
from brain_games.greetings import name
from random import randint, choice

print('What is the result of the expression?')


def game_calc():
    count = 0

    while count < 3:
        lst = ['+', '*', '-']
        operation = choice(lst)
        a = randint(1, 100)
        b = randint(1, 100)
        question = str(a) + ' ' + operation + ' ' + str(b)
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        correct_answer = eval(question)
        if answer == str(correct_answer):
            print('Correct!')
        elif answer != str(correct_answer):
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
        count += 1
    print(f'Congratulations, {name}!')
