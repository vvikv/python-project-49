from random import randint, choice


def game_progression():
    num1 = randint(2, 5)
    num2 = randint(30, 50)
    num3 = randint(3, 6)
    progression = list(range(num1, num2, num3))
    random_num = choice(progression)
    progression_pul = progression_les(progression, random_num)
    correct_answer = random_num
    question = " ".join(map(str, progression_pul))
    return correct_answer, question


def progression_les(progression, ran_num):
    for i in range(len(progression)):
        if progression[i] == ran_num:
            progression[i] = '..'
    return progression
