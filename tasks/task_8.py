user_line = [str(city) for city in input().replace(' ', '').split(',')]
k = int(input())
# user_line.sort(key=len)

# print(max(user_line, key=len))

citys = []
i = 1

while i < k:
    city = max(user_line, key=len)

    citys.append(city)
    user_line.remove(city)
    
    i += 1

print(citys)

# TODO ну, почти. Надо чтобы с нулевого user_line начиналось 
# --------------------------------------

# while i < user_counter:
#     city = max(user_line, key=len)

#     if city in citys:
#         continue
#     else:
#         citys.append(city)
    
    
#     i += 1