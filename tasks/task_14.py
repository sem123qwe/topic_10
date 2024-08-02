play_2048: list[str] = [int(num) for num in input().split()]
resalt: list = []
lenhgt = len(play_2048)

for i in play_2048:
    if i == 0:
        play_2048.remove(0)

num = 1

while num < len(play_2048):
    if play_2048[num] == play_2048[num - 1]:
        play_2048[num] = play_2048[num] + play_2048[num - 1]
        play_2048.remove(play_2048[num - 1])

    num += 1
    
while len(play_2048) < lenhgt:
    if len(play_2048) < lenhgt:
        play_2048.append(0)


print(play_2048)
