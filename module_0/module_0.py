import numpy as np


def game_core_v3(number):  # вход в цикл, проверяющий соответствие условиям
    count = 0          # счетчик попыток угадывания
    answer = ''        # указатель, больше или меньше задуманного очередное число
    higher_value = 101 # максимальное число
    lower_value = 1    # минимальное число

    # проверка на больше или меньше. Если числа guess и number совпали, программа вернет число попыток
    while count < 1000:
        count += 1
        if answer == 'less':
            higher_value = guess
        elif answer == 'more':
            lower_value = guess
        guess = int((lower_value + higher_value) / 2)

        if guess == number:
            return count
        elif guess > number:
            answer = 'less'
        elif guess < number:
            answer = 'more'


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_list = []
    np.random.seed(1)  # фиксируем RANDOM SEED
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_list.append(game_core(number))
    score = int(np.mean(count_list))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

# запускаем
score_game(game_core_v3)
