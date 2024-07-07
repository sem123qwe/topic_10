uset_line: list[str] = input().split()

alpha_list = []
numbers_list = []
float_list = []

for item in uset_line:
    if item.isalpha():
        alpha_list.append(item)
    elif item.isdigit():
        numbers_list.append(item)
    else:
        float_list.append(f'{item:0<}')


if alpha_list == False:
    print('Список целых чисел пуст')
else:
    print(numbers_list)

if float_list == False:
    print('Список вещественных чисел пуст')
else:
    print(float_list)

if alpha_list == False:
    print('Список остальных символов пуст')
else:
    print(alpha_list)


