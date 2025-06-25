# task4
# Користувач вводить із клавіатури числа. Програма повинна підраховувати суму, максимум і мінімум, введених чисел. Коли користувач вводить число 7 програма припиняє свою роботу і виводить на екран напис "Good bye!".

# sum = 0
# flag = True
# # 7 2 3 5 1
# while True:
#     number = int(input("Enter number :: "))
#     if number == 7:
#         print("Good bye!")
#         break
#     sum += number
#     if flag:
#         min = number
#         max = number
#         flag = False
#     if min > number:
#         min = number
#     if max < number:
#         max = number
# print(f"Sum :: {sum}")
# print(f"Min :: {min}")
# print(f"Max :: {max}")

# Завдання 6
# Напишіть програму, яка перевіряє, чи є введене користувачем число членом послідовності Фібоначчі.

# Принцип роботи програми:

# Програма повинна запитувати у користувача ціле число N .
# Якщо число N належить послідовності Фібоначчі, програма виводить повідомлення: "Число N належить послідовності Фібоначчі".
# Якщо число N не належить послідовності Фібоначчі, програма виводить повідомлення: "Число N не належить послідовності Фібоначчі".
# Що таке число Фібоначчі:
# Числа Фібоначчі — це числа, що утворюють послідовність, у якій кожне наступне число є сумою двох попередніх. Початкові значення: 0,1,1,2,3,5,8,13, і так далі.

# number = int(input("Enter number :: "))
# a = 0
# b = 1
# flag = False
# if number < 0:
#     print("Error! invalid value")
# else:
#     while a <= number:
#         if a == number:
#             flag = True
#         a,b = b, a + b
#     if flag:
#         print(f"Число {number} належить послідовності Фібоначчі")
#     else:
#         print(f"Число {number} не належить послідовності Фібоначчі")


# 0 1 2
# a = 0
# while a < 10:
#     b = 0
#     while b < 10:
#         c = 0
#         while c < 10:
#             if a != b and b != c and a != c:
#                 print(f"{a}{b}{c}")
#             c+=1
#         b+=1
#     a+=1
# line
# print("\t"*0,end="")
# print("*",end="")
# print("\t"*2,end="")
# print("*",end="")
# print("\t"*2,end="")
# print("*",end="")
# print("\t"*0,end="")
# print()
# # line2
# print("\t"*1)
# print("*")
# print("\t"*1)
# print("*")
# print("\t"*1)
# print("*")
# print("\t"*1)

# # line3
# print("\t"*2)
# print("*")
# print("\t"*0)
# print("*")
# print("\t"*0)
# print("*")
# print("\t"*2)

# # line 4
# print("*"*5)

# # line 5
# print("\t"*2)
# print("*")
# print("\t"*0)
# print("*")
# print("\t"*0)
# print("*")
# print("\t"*2)

# # line 6
# print("\t"*1)
# print("*")
# print("\t"*1)
# print("*")
# print("\t"*1)
# print("*")
# print("\t"*1)

# # line 7
# print("\t"*0)
# print("*")
# print("\t"*2)
# print("*")
# print("\t"*2)
# print("*")
# print("\t"*0)

# line = 11
# j = 0
# q = line // 2 - 1
# for i in range(line):
#     if i < line // 2:
#         print(" " * j + "*" + " " * q + "*" + " " * q + "*" + " " * j)
#         j+=1
#         q-=1
#     elif i == line // 2:
#         print("*"*line)
#     else:
#         j-=1
#         q+=1
#         print(" " * j + "*" + " " * q + "*" + " " * q + "*" + " " * j)

# *******
#  *****
#   ***
#    *   
        

