user_massege: list[str] = input().split()

max_num: int = 0
min_num: int | float = float('infinity')
resalt_max: str = ''
resalt_min: str = ''

for word in user_massege:
    word_length: int = len(word)

    if word_length > max_num:
        max_num = word_length
        resalt_max = word
    if word_length < min_num:
        min_num = word_length
        resalt_min = word

print(resalt_min, resalt_max, sep='\n')

# №2

user_massege: list[str] = input().split()
print(min(user_massege, key=len), max(user_massege, key=len), sep='\n')
