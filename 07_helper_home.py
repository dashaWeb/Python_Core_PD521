# Task 2
# Користувач вводить із клавіатури два числа (початок і кінець діапазону). Потрібно проаналізувати всі числа в цьому діапазоні. Потрібно вивести на екран:
# Усі числа діапазону.
# Усі числа діапазону в спадному порядку.
# Усі числа, кратні 7.
# Кількість чисел, кратних 5.

# start = int(input("Enter number :: ")) # 1
# end = int(input("Enter number :: ")) # 10

# if start > end:
#     start,end = end,start

# # Усі числа діапазону.
# print("Усі числа діапазону")
# i = start
# while i <= end:
#     print(i, end="\t")
#     i+=1
# print()
# print("Усі числа діапазону в спадному порядку.")
# # Усі числа діапазону в спадному порядку.
# i = end
# while i >= start:
#     print(i, end="\t")
#     i-=1
# print()

# print("Усі числа, кратні 7")
# i = start
# while i <= end:
#     if i % 7 == 0:
#         print(i, end="\t")
#     i+=1
# print()

# print("Кількість чисел, кратних 5")
# i = start
# counter = 0
# while i <= end:
#     if i % 5 == 0:
#         counter += 1
#     i+=1
# print(f"Кількість чисел, кратних 5 = {counter}")

# Task 5
# Користувач вводить два числа, що представляють діапазон. Програма повинна пройти по діапазону і вивести добуток усіх чисел, які діляться на 4, але не діляться на 6. Якщо таких чисел немає, вивести відповідне повідомлення. Діапазон має автоматично нормалізуватися, якщо початок більший за кінець.

# start = int(input("Enter number :: ")) # 1
# end = int(input("Enter number :: ")) # 10

# if start > end:
#     start,end = end,start
# i = start
# mult = 1
# while i <= end:
#     if i % 4 == 0 and i % 6 != 0:
#         mult *= i # mult = mult * i
#     i+=1
# print(f"Result :: {mult}")

# task 6
# Користувач вводить два числа: число A і ступінь N, у який потрібно піднести число. Програма повинна обчислити A у степені N за допомогою циклу (без використання вбудованих функцій піднесення до степеня).

# number = int(input("Enter number :: ")) # 2
# step = int(input("Enter number :: ")) # 4
# # 2^4 ==> 2 * 2 * 2 * 2
# mult = number
# step-=1
# while step > 0:
#     mult *= number # mult = mult * i
#     step-=1
# print(f"Result :: {mult}")