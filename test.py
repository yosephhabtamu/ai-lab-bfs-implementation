# import random

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# check = []

# # for i in range(500):
# #     left = ls[random.randint(0, 49)]
# #     right = ls[random.randint(0, 49)]
# #     coordinate = (left, right)
# #     if left == right:
# #         continue
# #     if (right, left) in check:
# #         continue
# #     if coordinate not in check:
# #         check.append(coordinate)
# #         print('edge Node_' + str(coordinate[0]), 'Node_' +
# #               str(coordinate[1]), random.randint(20, 100))
# #     if len(check) == 250:
# #         break
# # for i in range(1, 51):
# #     # print('node Node_'+str(i), 1)
# #     print(i)

# for i in range(51):
#     left = ls[random.randint(0, 49)]
#     right = ls[random.randint(0, 49)]
#     coordinate = (left, right)
#     if left == right:
#         continue
#     if (right, left) in check:
#         continue
#     if coordinate not in check:
#         check.append(coordinate)
#         print('heuristic Node_' + str(i), str(coordinate[0]),
#               str(coordinate[1]))
#
