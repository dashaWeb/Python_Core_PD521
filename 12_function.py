

# def sum_Numb(a,b):
#     return a + b
# res = sum_Numb(2,3)
# print(f"Average :: {res / 2}")

# print(res)

# def printMessage(first_name = "", last_name = ""):
#     print(f"Hello\n First name :: {first_name} \n Last name :: {last_name}")

# printMessage(last_name="Bondar")


def summ(a,b):
    return a + b
def summ(a,b,c = 0):
    return a + b + c

def sub(a, b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b == 0:
        print("Error! Division by zero!")
    else:
        return a / b

def calculate(a,b,op):
    match op:
        case '+':
            return summ(a,b)
        case '-':
            return sub(a,b)
        case '*':
            return mult(a,b)
        case '/':
            return div(a,b)
    print("Error! select true operation")

def searcOperation(line):
    if line.find('+') != -1:
        return '+'
    if line.find('-') != -1:
        return '-'
    if line.find('*') != -1:
        return '*'
    if line.find('/') != -1:
        return '/'

# a = int(input("Enter number :: "))
# b = int(input("Enter number :: "))
# print(f"{a} + {b} = {summ(a,b)}")
# print(f"{a} - {b} = {sub(a,b)}")
# print(f"{a} * {b} = {mult(a,b)}")
# print(f"{a} / {b} = {div(a,b)}")

# req = input("Enter :: ") # 2 + 2
# numbers = req.split(searcOperation(req))
# numbers = [int(i.strip()) for i in numbers]
# print(f"{numbers[0]} {searcOperation(req)} {numbers[1]} = {calculate(numbers[0],numbers[1],searcOperation(req))} ")

# def sum_all(*numbers):
#     sum = 0
#     for numb in numbers:
#         sum+=numb
#     return sum

# print("Sum:",sum_all(1,2,3,4,5,6,7,8,9))
def printMatrix(matr):
    for row in matr:
        for item in row:
            print(item, end="\t")
        print()

import random
matrix = [[random.randint(1,20) for i in range(4)] for j in range(4)]

printMatrix(matrix)