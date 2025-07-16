import random
prices = [random.randint(100, 500) for i in range(10)]


def printPrice(coll, prompt=""):
    print(prompt, end="") if len(prompt) > 0 else ""
    for item in coll:
        print(item, end="\t")
    print()


printPrice(prices, "Before :: ")

for i in range(len(prices)):
    prices[i] -= round((prices[i] * 0.05))
printPrice(prices, "After  :: ")


def upPrice(item):
    return item + (item * 0.10)


def my_map(list_):
    j = 0
    clone = list_.copy()
    for i in list_:
        clone[j] = upPrice(i)


printPrice(list(map(upPrice, prices)), "Up price :: ")


def convert(str):
    return int(str)


# marks = input("enter marks --> ").split()
# # marks = list(map(convert, marks))
# marks = list(map(lambda x : int(x), marks))
# marks = list(map(lambda item: item + 1 if item <= 11 else item, marks))
# print(marks)
# print(sum(marks) / len(marks))

showMessage = lambda : print("Hello")

showMessage()

sum_ = lambda a,b : a + b 
print(sum_(5,7))


printPrice(prices)

start = int(input("Enter start line :: "))
end = int(input("Enter end line :: "))

filter_list = list(filter(lambda x : x >= start and x <= end, prices))
printPrice(filter_list)