# Генераторы списков

# nums: list[int] = []
#
# n: int = 5
# for _ in range(n):
#     num: int = int(input())
#     nums.append(num)
#
#
# print(nums)

# ----------

# n: int = 5
# nums: list[int] = [int(input()) for _ in range(n)]

# nums: list[int] = [
#     int(input())
#     for _ in range(n)
# ]

# ----------
# data: list[str] = ['-54', '5', '77', '90', '-10']
#
# for i in range(len(data)):
#     data[i] = int(data[i])
#
# print(data)

# ----------

# data: list[str] = ['-54', '5', '77', '90', '-10']
# print(data)
# data: list[int] = [int(elem) for elem in data]
# print(data)

# ex: list[int] = [x for x in range(5)]

# ----------

# data: list[int] = [int(item) for item in input().split()]
# print(data)

# ----------

# data: list[str] = ['-54', '5', '77', '90', '-10']
#
# result: list[int] = []
# for item in data:
#     item = int(item)
#     if item >= 0:
#         result.append(item)
# print(result)
#
# # result_2: list[int] = [int(elem) for elem in data if int(elem) >= 0 if int(elem) < 50]
# result_2: list[int] = [int(elem) for elem in data if 0 <= int(elem) < 50]
#
# # result_2: list[int] = [
# #     int(elem)
# #     for elem in data
# #     if int(elem) >= 0
# # ]
#
# print(result_2)

# ----------

# data: list[str] = ['-54', '5', '77', '90', '-10']
# negatives: list[int] = []
# positives: list[int] = []
#
# for item in data:
#     item = int(item)
#
#     if -50 <= item < 50:
#         if item > 0:
#             positives.append(item)
#         else:
#             negatives.append(item)
# print(negatives)
# print(positives)
#
# negatives: list[int] = []
# positives: list[int] = []
#
# empty: list[None] = [positives.append(int(elem)) if int(elem) > 0 else negatives.append(int(elem))
#                      for elem in data if -50 <= int(elem) < 50]
#
# print(negatives)
# print(positives)

# ----------

# fruits: list[str] = ['apple', 'blueberry', 'pineapple', 'kiwi', 'banana']
#
# print(min(fruits, key=len))
# print(max(fruits, key=len))

# ----------

data: list[str] = ['-54', '5', '77', '90', '-10']
print(min(data, key=int))
print(max(data, key=int))

# ----------
