
# while умова:
#     тіло
# a == b

# i = 0
# while i < 10:
#     i+=1
#     print(f"{i} -- Hello")
# else:
#     print("Finally")

# print("============================")

# 10 9 8 7 6 5 4 3 2 1
# i = 10
# while i != 0:
#     print(i, end="\t")
#     i-=1
# print()

# i = 10
# while i >= 1:
#     print(i, end="\t")
#     i-=1
# print()

# i = 0
# while i < 10:
#     print(10 - i, end="\t")
#     i+=1
# print()


# number = int(input("Enter number : "))
# i = 0
# if i > 0:
#     while i <= number: # 0 1 2 3 4 5 ..... number
#         print(i, end="\t")
#         i+=1
# else:
#     while i >= number: # 0 -1 -2 -3 -4 ..... -number
#         print(i, end="\t")
#         i-=1

# print()

# while True:
#     answer = int(input("2 + 2 = "))
#     if answer == 4:
#         break
# # else:
# #     print("Finally")

# print("=======================")


# start = 20
# end = 0
# if start > end:
#     start, end = end, start
#     # temp = start
#     # start = end
#     # end = temp
# print(start,end)
# while start <= end:
#     if start % 2 == 0:
#         print(start, end="\t")
#     start += 1

# while start <= end:
#     start += 1
#     if start % 2 != 0:
#         continue
#     print(start,end="\t")


# i = 0
# while i < 5:
#     i += 1
#     color = input("Enter color :: ")
#     if len(color) <= 3:
#         continue
#     print(color)

# 1234
# 4321
number = int(input("Enter number :: "))
new_number = 0
while number != 0:
    digit = number % 10
    number //= 10
    new_number *= 10
    new_number += digit
else:
    print(new_number)
