import numpy as np


def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50
    min_number = 0  # устанавливаем нижнюю границу диапазона искомого числа
    max_number = 100  # устанавливаем верхнюю границу диапазона искомого числа
    while number != predict:
        count += 1
        if number > predict:
            min_number = predict
            # берем среднее число из диапазона
            predict = round((max_number + predict)/2)
        elif number < predict:
            max_number = predict
            # берем среднее число из диапазона
            predict = round((min_number + predict)/2)
    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# Проверяем
score_game(game_core_v3)
