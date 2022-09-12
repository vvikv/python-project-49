import prompt as prompt
from random import randint
from brain_games.greetings import name
from random import randint, choice

print('Find the greatest common divisor of given numbers.')


def game_progression():
    count = 0

    while count < 3:
        num1 = randint(2, 5)
        num2 = randint(20, 30)
        num3 = randint(3, 6)

        progression = list(range(num1, num2, num3))

        random_num = choice(progression)

        def progression_les():
            for i in range(len(progression)):
                if progression[i] == random_num:
                    progression[i] = '..'
            return progression

        correct_answer = random_num
        print('Question: ' + str(progression_les()))
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        elif answer != str(correct_answer):
            return print(f"""'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.
Let's try again, {name}!""")
        count += 1
    print(f'Congratulations, {name}!')
