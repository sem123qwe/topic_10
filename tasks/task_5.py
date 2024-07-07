numbers: list[int] = [int(num) for num in input().split()]
user_num: int = int(input())

counter: int = 0
for i in numbers:
    if i > user_num:
        counter += 1

if not counter:
    print(-1)
else:
    print(counter)

# №2
# TODO: Можно решить в одну строку, используя генератора списка
