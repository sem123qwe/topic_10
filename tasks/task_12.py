user_massege = [int(num) for num in input().split()]
resalt = []

i = 0
j = 1 
k = len(user_massege)

while i < len(user_massege):
    if k > len(user_massege):
        k = 0

    summa = user_massege[i] + user_massege[k] + user_massege[j]
    resalt.append(summa)

    i += 1
    j += 1
    k += 1

print(resalt)