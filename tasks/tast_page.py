user_choose = input()

weather_data_for_year: list[list[int]] = [
    [-33, -28, -18, -39, -39, -21, -20, -40,
    -25, -12, -35, -10, -15, -14, -22, -34,
    -34, -22, -30, -24, -23, -20, -18, -12,
    -25, -20, -29, -27, -13, -12, -31],

    [-33, -21, -21, -27, -23, -30, -21,
    -16, -27, -31, -37, -20, -31, -24,
    -15, -24, -31, -33, -14, -19, -31,
    -38, -34, -18, -38, -17, -32, -26],

    [-12, -1, -3, -8, -14, 4, -17, 9,
    11, -6, -8, -5, 7, -9, -19, 12,
    -14, -2, 1, 10, -18, 5, -5,
    -11, -10, 9, -17, 0, 8, 3, 11],

    [13, 6, 14, 11, 9, 12, 9, 14,
    8, 15, 16, 15, 14, 10, 8, 8,
    9, 5, 10, 7, 17, 8, 15, 17,
    12, 13, 9, 10, 8, 7],

    [18, 14, 19, 16, 19, 16, 21, 15,
    13, 13, 21, 15, 14, 17, 21, 14,
    21, 19, 20, 21, 21, 18, 12, 17,
    16, 15, 16, 20, 19, 19, 21],

    [21, 23, 21, 18, 19, 18, 18, 19,
    23, 19, 21, 24, 16, 19, 23, 16,
    19, 19, 22, 20, 16, 19, 22, 21,
    16, 20, 20, 19, 16, 24],

    [21, 32, 27, 24, 20, 25, 23, 27,
    23, 21, 26, 31, 32, 28, 26, 22,
    29, 21, 20, 30, 20, 21, 26, 20,
    21, 22, 32, 21, 20, 22, 32],

    [32, 25, 31, 33, 29, 36, 25, 30,
    33, 26, 35, 33, 29, 32, 36, 28,
    26, 35, 28, 28, 35, 26, 31, 30,
    33, 32, 35, 33, 27, 27, 26],

    [13, 16, 18, 15, 19, 13, 13, 20,
    18, 14, 20, 17, 16, 16, 15, 16,
    13, 18, 16, 14, 18, 13, 17, 13,
    14, 19, 17, 13, 19, 13],

    [12, 12, 8, 4, 5, 12, 5, 7,
    4, 5, 8, 5, 5, 13, 8, 3,
    8, 5, 4, 10, 12, 2, 10, 4,
    2, 1, 13, 3, 4, 2, 12],

    [2, -5, -7, -9, -4, -7, 5, -3,
    -1, -7, 4, 4, 3, 4, -5, -6,
    -4, -9, -5, -10, -6, -3, -1, -1,
    0, 2, -7, -5, -7, 0],

    [-19, -23, -24, -21, -19, -20, -17, -23,
    -16, -24, -20, -21, -25, -20, -24, -22,
    -17, -23, -16, -22, -18, -16, -25, -26,
    -21, -19, -19, -23, -23, -17]
]




for i in range(len(weather_data_for_year)):
    
    weather_data_for_year[i] = sum(weather_data_for_year[i]) / len(weather_data_for_year[i])

# Создайте список с названиями месяцев
monts = [ 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

if user_choose.lower() == "год":
    print(f'Среднегодовая температура: {round(sum(weather_data_for_year) / 12, 2)} C.')
elif user_choose.lower() in monts:
    for i in range(len(monts)):
        if user_choose.lower() in monts:
            a = monts.index(user_choose.lower())
    print(f'Средняя температура за {user_choose.lower()}: {round(weather_data_for_year[a], 2)} C.')


