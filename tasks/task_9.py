user_massege = [int(num) for num in input().split()]

i = 0
j = 1
lenght = len(user_massege)
resalt = []

while j < lenght:
    if user_massege[j] > user_massege[i]:
        resalt.append(user_massege[j])
    i += 1
    j += 1
        
print(str(resalt) or False)

# ----------------------------------
