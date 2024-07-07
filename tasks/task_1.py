resalt: str = ''

user_input: list[str] = input().split()

for item in user_input:
    if user_input == 'конец':
        break
    
    if user_input[0].lower() == 'конец':
            print('Ничего не введено')

    else:
        resalt += item + ','

print(resalt)

