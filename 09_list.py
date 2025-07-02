# test = [True,"Test",145,145.2]
# print(test)

colors = ["red","purple","yellow","orange","blue"]
print(f"Id: {id(colors)} \t Type: {type(colors)} \t Value : {colors} \t Length: {len(colors)}")
print(colors[2])

colors[2] = "lime"
print(colors[2])
# colors[5] = "pink" Error

# [start:end:step]
print(colors[2:])
print(colors[:2])
print(colors[::2])
# i = 0
# while i < len(colors):
#     print(colors[i])
#     i+=2
print(colors[::-1]) #reverse


for item in colors:
    print(item.upper())

# Додає новий елемент в кінець списку
print('list.append()')
print(f"Before :: {colors}")
colors.append("green")
print(f"After  :: {colors}")

# Додає новий елемент за вказаним індексом
print('list.insert(2,"gold")')
print(f"Before :: {colors}")
colors.insert(2,"gold")
print(f"After  :: {colors}")


# Додає список до поточного списку
print('list.extend()')
print(f"Before :: {colors}")
colors.extend(["magenta","brown","cyan"])
print(f"After  :: {colors}")

# Видаляє елемент зі списку за індексом
print('list.pop()')
print(f"Before :: {colors}")
colors.pop()
print(f"After  :: {colors}")

# Видаляє елемент зі списку за індексом
print('list.pop()')
print(f"Before :: {colors}")
colors.pop(2)
print(f"After  :: {colors}")

# Видаляє елемент списку за вмісто
print('list.remove("lime")')
print(f"Before :: {colors}")
colors.remove("lime")
print(f"After  :: {colors}")


print(f"Before :: {colors}")
if 'pink' in colors:
    colors.remove("pink")
print(f"After  :: {colors}")

# colors.clear()
# print(colors)

print(f'List :: {colors}')
print(f"Index :: {colors.index("green")}")


print(f'List :: {colors}')
print(f"count :: {colors.count("green")}")

# [a - z]
colors.sort()
print(colors)

# [z - a]
colors.sort(reverse=True)
print(colors)

colors.reverse()
print(colors)

number = [1,2,3,11,5,6,7]
print(min(number))
print(max(number))
print(sum(number))
print(sorted(number))
print(sorted(number,reverse=True))
number_str = '-'.join(colors)
print(number_str)

numbers_2 = number.copy()

print(f"{number} ID :: {id(number)}")
print(f"{numbers_2} ID :: {id(numbers_2)}")

numbers_2[0] = 333
print(f"{number} ID :: {id(number)}")
print(f"{numbers_2} ID :: {id(numbers_2)}")

number_str = [str(item) for item in number]
# for numb in number:
#     number_str.append(str(numb))
print(' - '.join(number_str))

# marks =[int(i) for i in input("Enter marks :: ").split(" ")]
# print(marks)


numbers = [1,2,3,4,5,6,7,8,5,4,21,4,5]
unique = []
for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)
print(unique)