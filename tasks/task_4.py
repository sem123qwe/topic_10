spicok = input().split()
resalt = []
a = spicok.extend(resalt)

for i in spicok:
    counter = spicok.count(i)

    if counter > 1:
        if i in resalt:
            continue
        else:
            resalt.append(i)
    else:
        resalt.append(i)

print(f'ID списка: [{id(spicok)}] \nИсходный список: {spicok}')
print(f'ID списка: [{id(resalt)}] \nИсходный список: {resalt}')

difference = len(spicok) - len(resalt)
if difference == 0:
    print('В списке не найдено дубликатов')
else:
    print(f'Удалено {difference} дубликатов')


# TODO с айпишником надо подумать ! (extend)