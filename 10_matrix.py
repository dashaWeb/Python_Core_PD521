
# matrix = [
#     [1,2,3, 5, 50, 75,85,105], #0
#     [4,5,6, 5, 25, 50, 75], #1
#     [7,8,9, 5, 25, 50, 75],  #2
#     [10,11,12, 5, 25, 50, 75],  #2
#     [13,14,15, 5, 25, 50, 75],  #2
#     [16,17,18, 5, 25, 50, 75],  #2
# ]

#row 1 
# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[0][2])

#row 1 
# for i in range(3): # 0 1 2
#     print(matrix[0][i], end="\t")
# print()
# #row 2 
# for i in range(3): # 0 1 2
#     print(matrix[1][i], end="\t")
# print()
# #row 3 
# for i in range(3): # 0 1 2
#     print(matrix[2][i], end="\t")
# print()
# len()

# print(len(matrix))
# Print Matrix
# for j in range(len(matrix)): # 0 1 2 проходимо порядках
#     for i in range(len(matrix[j])): # 0 1 2 проходимо по комірках
#         print(matrix[j][i], end="\t") 
#     print()

#
# row = 3
# col = 3

# row,col = 3,3
# import random
# row = col = 3
# matrix = []

# for i in range(row):
#     row_matrix = []
#     for j in range(col):
#         row_matrix.append(random.randint(1,20))
#     matrix.append(row_matrix)

# for j in range(len(matrix)): # 0 1 2 проходимо порядках
#     for i in range(len(matrix[j])): # 0 1 2 проходимо по комірках
#         print(matrix[j][i], end="\t") 
#     print()


# import random
# row = col = 3


# row_1 = [random.randint(1,20) for i in range(col)]
# row_2 = [random.randint(1,20) for i in range(col)]
# row_3 = [random.randint(1,20) for i in range(col)]

# matrix = [
#     row_1,
#     row_2,
#     row_3
# ]
# for j in range(len(matrix)): # 0 1 2 проходимо порядках
#     for i in range(len(matrix[j])): # 0 1 2 проходимо по комірках
#         print(matrix[j][i], end="\t") 
#     print()

# import random
# row = col = 3

# matrix = []

# for i in range(row):
#     matrix.append([random.randint(1,20) for i in range(col)])


# for j in range(len(matrix)): # 0 1 2 проходимо порядках
#     for i in range(len(matrix[j])): # 0 1 2 проходимо по комірках
#         print(matrix[j][i], end="\t") 
#     print()

# import random
# row = 4
# col = 5

# matrix = [[random.randint(1,20) for i in range(col)] for j in range(row)]


# for row in matrix:
#     for item in row:
#         print(item, end="\t")
#     print()

# import random
# row = 3
# col = 3

# matrix = [[random.randint(1,5) for i in range(col)] for j in range(row)]



# # print matrix
# for row in matrix:
#     for item in row:
#         print(item, end="\t")
#     print()

# # Sum all elements
# # sum_ = 0
# # for row in matrix:
# #     for item in row:
# #         sum_+= item

# # print(f"Sum :: {sum_}")
# sum_ = 0
# for row in matrix:
#     sum_ += sum(row)
# print(f"Sum :: {sum_}")


# # Min MAx 
# max_ = matrix[0][0]
# min_ = matrix[0][0]
# # for row in matrix:
# #     for item in row:
# #         if max_ < item:
# #             max_ = item
# #         if min_ > item:
# #             min_ = item

# for row in matrix:
#         if max_ < max(row):
#             max_ = max(row)
#         if min_ > min(row):
#             min_ = min(row)

# print(f"Min :: {min_}")
# print(f"Max :: {max_}")


import random
# row = 3
# col = 3

# matrix = [[random.randint(1,20) for i in range(col)] for j in range(row)]
# # print matrix
# for row in matrix:
#     for item in row:
#         print(item, end="\t")
#     print()


# clone = matrix.copy()
# for i in range(len(matrix)):
#     clone[i] = matrix[i].copy()

# print(f"Origin :: {matrix}")
# print(f"Clone  :: {clone}")

# print(f"Origin :: {id(matrix)}")
# print(f"Clone  :: {id(clone)}")

# clone[0][0] = 22
# print(f"Origin :: {matrix}")
# print(f"Clone  :: {clone}")


# row_ = 3
# col = 4

# matrix = [[random.randint(1,20) for i in range(col)] for j in range(row_)]


# sum_total = 0

# for row in matrix:
#     sum_ = 0
#     for item in row:
#         print(item, end="\t")
#         sum_ += item
#     print(f"|  {sum_}")

# print("-"*(8*col + 5) )

# for j in range(col):
#     sum_ = 0
#     for i in range(row_):
#         sum_+= matrix[i][j]
#     sum_total+= sum_
#     print(sum_, end="\t")

# print(f"|  {sum_total}")


box = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
]
for b in box:
    for r in b:
        for c in r:
            print(c,end="\t")
        print()
    print()