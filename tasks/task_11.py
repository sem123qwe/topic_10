line: str = input()
repetitions = []

lenght = len(line)

for i in line:
    for j in line:
        if range(line[i]) != range(line[j]) and i == j:
            repetitions.append(i)

# print(repetitions)

# for i in line: 
#     if i in repetitions:
#         repetitions.remove(i)
#     elif i not in repetitions:
#         repetitions.append(i)

# for i in range(line):
#     for j in range(line):
#         if line[i] == line[j] and i != j:
#             repetitions.append(i)

# print(repetitions)





