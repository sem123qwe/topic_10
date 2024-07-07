like: list[str] = input().split()


counter_liked: int = len(like)
cool: str = 'понравилось это'
if counter_liked is False:
    print('никто не оценил это')
elif counter_liked == 1:
    print(f'{like[0]} {cool}')
elif counter_liked == 2:
    print(f'{like[0]} и {like[1]} {cool}')
elif counter_liked == 3:
    print(f'{like[0]}, {like[1]} и {like[2]} {cool}')
else:
    print(f'{like[0]}, {like[1]} и ещё {counter_liked - 2} {cool}')














