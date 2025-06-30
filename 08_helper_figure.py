# *****
#  ***
#   *
#  ***
# *****

# print(" " * 0 + "*" * 5)
# print(" " * 1 + "*" * 3)
# print(" " * 2 + "*" * 1)
# print(" " * 1 + "*" * 3)
# print(" " * 0 + "*" * 5)

#  д
# i = 0
# line = 5
# j = line
# for q in range(line):
#     if q == line // 2 + 1:
#         i-=1
#         j+=2
#     if q < line // 2 + 1:
#         print(" " * i + "*" * j)
#         i+=1
#         j-=2
#     else:
#         i-=1
#         j+=2
#         print(" " * i + "*" * j)

# б
# *
# **
# ***
# ****
# *****
# print("*"*1)
# print("*"*2)
# print("*"*3)
# print("*"*4)
# print("*"*5)
# line = 11
# for i in range(line):
#     print("*"*(i + 1))

# line = 11
# while line > 0:
#     print("*"*(line))
#     line-=1

line = 15
i = 0
for q in range(line):
    if q < line // 2 + 1:
        i+=1
        print("*" * i)
    else:
        i-=1
        print("*" * i)