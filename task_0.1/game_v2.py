"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    count = 0
    mn_numb = 1 # Минимальное значение рассматриваемого интервала
    mx_numb = 100 # Максимальное значение рассматриваемого интервала

    while True:
        count += 1
        if predict_number > number:
            mx_numb = predict_number - 1
            predict_number = (mx_numb + mn_numb) // 2
        elif predict_number < number:
            mn_numb = predict_number + 1
            predict_number = (mx_numb + mn_numb) // 2
        else:
            break # конец игры и выход из цикла
    return (count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return (score)


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
