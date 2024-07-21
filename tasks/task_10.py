user_line = input().split()
unic_num = []
lenght = len(user_line)

# for i in range(user_line):
#     for j in range(user_line):
#         if user_line[i] == user_line[j] and i != j:
#             unic_num.append(i)

for i in user_line:
    if i in unic_num:
        unic_num.remove(i)
    else:
        unic_num.append(i)

print(unic_num)

