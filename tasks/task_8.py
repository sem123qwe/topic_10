user_line: list[str] = [city for city in input().split(', ')]
k: int = int(input())

user_line.sort(key=len, reverse=True)
print(user_line[:k])

# №2

i: int = 0
result: list[str] = []
while i < k:
    result.append(user_line[i])
    i += 1

print(result)
