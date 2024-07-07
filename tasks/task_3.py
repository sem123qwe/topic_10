like: list[str] = input().split()

counter_liked: int = len(like)
cool: str = 'понравилось это'
if not counter_liked:
    print('никто не оценил это')
elif counter_liked == 1:
    print(f'{like[0]} {cool}')
elif counter_liked == 2:
    print(f'{like[0]} и {like[1]} {cool}')
elif counter_liked == 3:
    print(f'{like[0]}, {like[1]} и {like[2]} {cool}')
else:
    print(f'{like[0]}, {like[1]} и ещё {counter_liked - 2} человека {cool}')

# №2

likes: list[str] = input().split()

if not likes:
    print('никто не оценил это')
else:
    users_count: int = len(likes)
    if users_count >= 4:
        first_user, second_user, *other_users = likes
        out_line: str = (f'{first_user}, '
                         f'{second_user} и ещё '
                         f'{len(other_users)} человека')
    elif users_count == 3:
        first_user, second_user, third_user = likes
        out_line: str = (f'{first_user}, {second_user} и {third_user}')
    else:
        out_line: str = ' и '.join(likes)

    print(f'{out_line} понравилось это')
