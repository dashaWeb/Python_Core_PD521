
# print(3,type(3)) # number (int)
# print(3.5,type(3.5)) # number (float)
# print("Hello",type("Hello")) # string (str)
# print(True, type(True)) # boolean (bool)


# # 2test
# # test2

# first_name = "Denis"
# lastName= "Bondar"
# age = 18
# PI = 3.14
# flag = True

# print(first_name,type(first_name))
# print(lastName,type(lastName))
# print(age,type(age))
# print(PI,type(PI))
# print(flag,type(flag))

# lastName = "Demchuk"
# print(lastName,type(lastName))
# # PI = 3.18
# # print(PI,type(PI))

# print(first_name,lastName,age,PI,flag)
# print(first_name+lastName,+age+PI+flag) #TypeError: can only concatenate str (not "int") to str
# print(first_name+lastName) 
# print(age + PI)

# '''
#     /
#     *
#     +
#     -
#     %
#     //
#     **

#     Priority
#         ()
#         **,//,%
#         /,*
#         +,-
# '''

# print('''
# Enter
#         Tab
#                 Text''')

# # num_1 = 7
# # num_2 = 5
# num_1, num_2 = 8, 5
# res_sum = num_1 + num_2
# # 7 + 5 = 12
# # print(num_1,"+",num_2,"=",res_sum)
# # print("{} + {} = {}".format(num_1,num_2,res_sum))
# print(f"{num_1} +  {num_2} = {num_1 + num_2}") #12
# print(f"{num_1} -  {num_2} = {num_1 - num_2}") #2
# print(f"{num_1} *  {num_2} = {num_1 * num_2}") #35
# print(f"{num_1} /  {num_2} = {num_1 / num_2}") #1.6
# print(f"{num_1} // {num_2} = {num_1 // num_2}") #1
# print(f"{num_1} %  {num_2} = {num_1 % num_2}") #3
# num_1 = 2
# num_2 = 4
# print(f"{num_1} ** {num_2} = {num_1 ** num_2}") #16


# num_1 = 2.5
# num_2 = 4.6
# print(f"{num_1} %  {num_2} = {num_1 % num_2}") #1


# Завдання 1
# Користувач вводить з клавіатури два числа. Необхідно знайти суму чисел, різницю чисел, добуток числі. Результат обчислень вивести на екран.
# True(1) False(0)
# result = False + 1 + 3.14
# print(result, type(result))

# line_int = "324"
# line_float = "32.9"
# integer = int(line_int) + 23
# number_float = float(line_float)
# print(integer, type(integer))
# print(number_float, type(number_float))
# print(int(number_float))
# flag = bool(0)
# number = str(number_float)
# print(flag, type(flag))
# print(number, type(number))

# Завдання 1
# Користувач вводить з клавіатури два числа. Необхідно знайти суму чисел, різницю чисел, добуток числі. Результат обчислень вивести на екран.
# number_1 = int(input("Enter number : "))
# number_2 = input("Enter number : ")
# number_2 = int(number_2)
# print(f"{number_1} + {number_2} = {number_1 + number_2}")
# print(f"{number_1} - {number_2} = {number_1 - number_2}")
# print(f"{number_1} * {number_2} = {number_1 * number_2}")

# Завдання 5
# Напишіть програму, яка перетворює довжину з метрів у сантиметри. Користувач вводить значення довжини в метрах, програма має обчислити та вивести на екран результат у сантиметрах. Нагадайте, що 1 метр = 100 сантиметрів.

m = input("Enter meters :: ")
sm = int(m) * 100
print(f"{m}m = {sm}sm")
