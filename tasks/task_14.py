play_2048: list[int] = [int(num) for num in input().split()]

length: int = len(play_2048)
play_2048: list[int] = [num for num in play_2048 if num != 0]

i: int = 1
while i < len(play_2048):
    if play_2048[i] == play_2048[i - 1]:
        play_2048[i] = play_2048[i] + play_2048[i - 1]
        del play_2048[i - 1]
    i += 1

zeros: list[int] = [0] * (length - len(play_2048))
play_2048.extend(zeros)

# while len(play_2048) < length:
#     play_2048.append(0)

print(play_2048)
