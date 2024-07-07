nums: list[int] = [int(num) for num in input().split()]
target: int = int(input())

removed_count: int = 0
while target in nums:
    nums.remove(target)
    removed_count += 1

if not nums:
    print('Пустой список')
elif not removed_count:
    print('Элемент не найден')
else:
    print(f'Удалено {removed_count} элементов\nНовый список: {nums}')
