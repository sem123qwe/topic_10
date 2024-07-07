line: list[str] = input().split()

numbers: list[int] = []
floats: list[float] = []
other_chars: list[str] = []

for item in line:
    temp_item = item[1:] if item.startswith(('+', '-')) else item
    if temp_item.isdigit():
        numbers.append(int(item))
    elif temp_item.replace('.', '', 1).isdigit():
        floats.append(float(item))
    else:
        other_chars.append(item)

print(numbers or 'Список целых чисел пуст')
print(floats or 'Список вещественных чисел пуст')
print(other_chars or 'Список остальных символов пуст')
