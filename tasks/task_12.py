nums: list[int] = list(map(int, input().split()))
repetitions: list[int] = []

length: int = len(nums)
for i in range(length):
    left: int = i - 1
    right: int = (i + 1) % length

    # TODO: Продолжите решение
