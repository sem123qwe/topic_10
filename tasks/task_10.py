nums: list[int] = list(map(int, input().split()))
unique_nums: list[int] = []

length: int = len(nums)
for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            break
    else:
        unique_nums.append(nums[i])

print(' '.join(map(str, unique_nums)) or False)
