# Завдання 2
# Напишіть програму, яка перевіряє, чи існує файл data.txt, і виводить відповідне повідомлення. Якщо файл існує, відкрийте його і виведіть кожен другий рядок у консоль.

# try:
#     with open("16_file/data.txt") as file:
#         lines = file.readlines()
#         for line in lines[1::2]:
#             print(line)
# except Exception as msg:
#     print(msg)


# Завдання 5
# Напишіть програму, яка аналізує файл log.txt, визначає 10 найпоширеніших слів, що зустрічаються найчастіше, і записує їх разом з їхньою частотою в word_stats.txt.
import re
list_words = []
list_numbers = []
try:
    with open("16_file/data.txt") as file:
        text = file.read()
    words = re.findall('\w+',text)
    for i in range(len(words)):
        flag = True
        for j in range(i):
            if words[i] == words[j]:
                flag = False
                break
        if flag:
            list_words.append(words[i])
            list_numbers.append(words.count(words[i]))
    with open("16_file/word_stats.txt",'w') as file: 
        for i in range(10):
            max_ = max(list_numbers) 
            index_ = list_numbers.index(max_)
            file.write(f"{list_words[index_]} :: {list_numbers[index_]} \n")
            list_numbers.pop(index_)
            list_words.pop(index_)      
except Exception as msg:
    print(msg)