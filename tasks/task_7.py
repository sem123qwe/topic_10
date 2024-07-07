user_massege: list[str] = input().split()

resalt_max: str = ''
max_num: int = 0
resalt_min: str = ''

min_num: int = len(user_massege[0])
lenght: int = len(user_massege)
i = 0
# TODO: Заменить на for
while i < lenght:
    if len(user_massege[i]) > max_num:
        max_num = len(user_massege[i])
        resalt_max = user_massege[i]
    if len(user_massege[i]) < min_num:
        min_num = len(user_massege[i])
        resalt_min = user_massege[i]
    i += 1

print(resalt_min)
print(resalt_max)

# TODO: Можно решить в одну строку, используя встроенные функции min и max
