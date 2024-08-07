sides: list[str] = input().split('x')

dimensions: list[int] = [int(side) for side in sides]
stars: list[str] = ['*' for _ in range(dimensions.pop())]
dimensions.reverse()

for dimension in dimensions:
    stars: list[list[str]] = [stars[:] for _ in range(dimension)]

for first in stars:
    if isinstance(first, list):
        for second in first:
            if isinstance(second, list):
                for third in second:
                    print(third, end=' ')
                print()
            else:
                print(second, end=' ')
        print()
    else:
        print(first, end=' ')

# Лучше реализовать через рекурсию.
