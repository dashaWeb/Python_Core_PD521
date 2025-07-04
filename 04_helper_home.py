# Завдання 6
# Користувач вводить два тризначні числа. Напишіть програму, яка:

# Об'єднує їх таким чином, щоб перша цифра взята з першого числа, друга цифра – з другого числа, третя цифра – знову з першого числа, і так далі.

# Виводить отримане шестизначне число.

# Приклад:

# Вхідні дані: перше число – 123, друге число – 456.
# Результат: об'єднане число – 142536.
# У цьому прикладі перша цифра "1" взята з першого числа, друга цифра "4" – з другого числа, третя цифра "2" – з першого, і так далі.

num_1 =  int(input("Enter number --> ")) # 123
num_2 =  int(input("Enter number --> ")) # 456

# 142536
print(f"num1 - {num_1} \t num2 - {num_2}")

numb_1_3 = num_1 % 10  # 123 % 10 --> 3
num_1 //= 10  # 123 / 10 --> 12.3 --> 12
numb_1_2 = num_1 % 10  # 12 % 10 --> 2
num_1 //= 10  # 12 // 10 = 1
numb_1_1 = num_1 % 10  # 1 % 10 --> 1
num_1 //= 10  # 1 // 10 --> 0

numb_2_3 = num_2 % 10  # 456 % 10 --> 6
num_2 //= 10  # 456 // 10 --> 45
numb_2_2 = num_2 % 10  # 45 % 10 --> 5
num_2 //= 10  # 45 // 10 --> 4
numb_2_1 = num_2 % 10  # 4 % 10 --> 4
num_2 //= 10  # 4 // 10 --> 0

res = 0
res *= 10  # 0 * 10 -> 0
res += numb_1_1  # 0 + 1 --> 1

res *= 10  # 1 * 10 -> 10
res += numb_2_1  # 10 + 4 --> 14

res *= 10  # 14 * 10 --> 140
res += numb_1_2  # 140 + 2 --> 142

res *= 10  # 142 * 10 --> 1420
res += numb_2_2  # 1420 + 5 --> 1425

res *= 10  # 1425 * 10 --> 14250
res += numb_1_3  # 14250 + 3 --> 14253

res *= 10  # 14253 * 10 --> 142530
res += numb_2_3  # 142530 + 6 --> 142536

print(f"Result :: {res}")
print(numb_1_1 * 100000 + numb_2_1 * 10000 + numb_1_2 * 1000 + numb_2_2 * 100 + numb_1_3 * 10 + numb_2_3)
