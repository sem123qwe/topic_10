numbers = input().split()
user_num = input()
counter = 0

for i in numbers:
    if i > user_num:
        counter += 1

if counter == 0:
    print('-1')
else:
    print(counter)






