nums: list[int] = list(map(int, input().split()))
repetitions: list[int] = []

length: int = len(nums)

for i in range(length):
    for j in range(length):
        if nums[i] == nums[j] and i != j:
            repetitions.append(nums[i])

print(' '.join(map(str, repetitions)) or False)
