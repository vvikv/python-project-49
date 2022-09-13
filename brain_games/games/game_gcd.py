from random import randint


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def game_gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = str(num1) + ' ' + str(num2)
    correct_answer = gcd(num1, num2)
    return correct_answer, question
