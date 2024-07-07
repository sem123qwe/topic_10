massege: list[str] = input().split()

for index, element in enumerate(massege):
    print(f'{element} {index}', end='\n')

# №2
for i in range(len(massege)):
    print(massege[i], i, end='\n')
