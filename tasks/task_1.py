user_input: str = input()

result: list[str] = []

for item in user_input:
    if user_input == 'конец':
        break

    if user_input[0].lower() == 'конец':
        print('Ничего не введено')

    else:
        result += item + ','

print(result)
