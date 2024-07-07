nums: list[int] = [int(num) for num in input().split()]
print(f'ID списка: [{id(nums)}] \nИсходный список: {nums}')

before_length: int = len(nums)
i: int = 0
was_seen: list[int] = []
while i < len(nums):
    if nums[i] in was_seen:
        del nums[i]
    else:
        was_seen.append(nums[i])
        i += 1

after_length: int = len(nums)

print(f'ID списка: [{id(nums)}] \nИзмененный список: {nums}')

if before_length - after_length:
    print(f'Удалено {before_length - after_length} дубликатов')
else:
    print('В списке не найдено дубликатов')
