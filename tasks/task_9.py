nums: list[int] = [int(num) for num in input().split()]

index: int = 1
length: int = len(nums)
result: list[int] = []

while index < length:
    if nums[index] > nums[index - 1]:
        result.append(nums[index])
    index += 1

# print(*result or False)
print(' '.join(map(str, result)) or False)
# print(' '.join([str(num) for num in result]) or False)
