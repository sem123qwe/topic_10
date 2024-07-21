numbers: list[int] = [int(num) for num in input().split()]
user_num: int = int(input())

counter: int = 0
for i in numbers:
    if i > user_num:
        counter += 1

print(counter or -1)

# №2

print(len([1 for elem in numbers if elem > user_num]) or -1)
print(sum([1 for elem in numbers if elem > user_num]) or -1)
