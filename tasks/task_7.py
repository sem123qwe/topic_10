user_massege: list[str] = input().split()

resalt_max: list = []
max_num: int = 0
resalt_min: list = []
min_num: int = len(user_massege[0])


lenght: int = len(user_massege)
i = 0

while i < lenght :
    if min_num > max_num:
        max_num = min_num

    
    if lenght > max_num:
        max_num = lenght
        resalt_max.clear()
        resalt_max.append(user_massege[i])
    
    if lenght < min_num:
        min_num = lenght
        resalt_min.clear()
        resalt_min.append(user_massege[i])

    i += 1

print(resalt_min)
print(resalt_max)

        







