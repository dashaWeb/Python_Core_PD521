# word = "Hello"
# for letter in word: #[H, e, l, l, o]
#     print(letter + " - ", end="")

# end = 10
# for i in range(end): # [0,1,2,3,4,5,6,7,8,9]
#     print(i + 1, end="\t")

# end = 10
# start = 1
# for i in range(start, end + 1): # [1,2,3,4,5,6,7,8,9,10]
#     print(i, end="\t")



# numb = int(input('Enter number :: ')) # 1,2,3, ..... numb
# for i in range(1, numb + 1):
#     print(i, end="\t")

# numb = int(input('Enter number :: ')) # 1,3,5,7,9 ... numb
# for i in range(1, numb + 1, 2):
#     print(i, end="\t")
#     if i == 5:
#         break
# else:
#     print("Finally")

# print("---------------------------")

# numb = int(input('Enter number :: ')) # 1,3,5,7,9 ... numb
# for i in range(1, numb + 1, 2):
#     if i % 5 == 0:
#         continue
#     print(i, end="\t")
# else:
#     print("Finally")

# print("---------------------------")


# numb = int(input("Enter number ::  ")) #8
# counter = 0
# # range(1,numb + 1) [1,2,3,4,5,6,7,8]
# # numb{8} % 1 == 0 ==> True (counter{0} += 1 (counter{1}))
# # numb{8} % 2 == 0 ==> True (counter{1} += 1 (counter{2}))
# # numb{8} % 3 == 0 ==> False ()
# # numb{8} % 4 == 0 ==> True (counter{2} += 1 (counter{3}))
# # numb{8} % 5 == 0 ==> False ()
# # numb{8} % 6 == 0 ==> False ()
# # numb{8} % 7 == 0 ==> False ()
# # numb{8} % 8 == 0 ==> True (counter{3} += 1 (counter{4}))
# for  i in range(1,numb+1):
#     if numb % i == 0:
#         counter+=1
# print(counter)

# if counter > 2:
#     print('Complex number')
# else:
#     print('Prime number')


# numb = int(input("Enter number ::  "))
# flag = True
# if numb > 2:
#     for i in range(2,numb//2):
#         if numb % i == 0:
#             flag = False
#             break
# if not flag:
#     print('Complex number')
# else:
#     print('Prime number')

import random

# for i in range(5):
#     # rnd = random.random() # 0 - 1
#     # rnd = int(random.random() * 10 + 1) # 1 - 10
#     # rnd = random.randint(1,10)
#     rnd = random.choice("srp")
#     print(rnd)
#     input()
user_win = 0
bot_win = 0
draw = 0
while True:
    bot_score = 0
    user_score = 0
    for i in range(5):
        print(f"{'-'*15} Round #{i+1} {'-'*15}")
        while True:  
            user = input('''
            [r] - rock
            [s] - scissors
            [p] - paper
            [v] - spock
            [l] - lizard
                Enter your choice :: ''')
            if user == 'r' or user == 'p' or user == 's' or user == 'v' or user == 'l':
                break
            else:
                print("\033[31m Error. Enter true choice \033[0m")

        bot = random.choice('srplv')

        print("\t\t Bot \t User")
        print(f"\t\t [{bot}] \t [{user}]")

        if user == 's' and bot == 'p' or user == 's' and bot == 'l' or user == 'p' and bot == 'r' or user == 'p' and bot == 'v' or user == 'r' and bot == 's' or user == 'r' and bot == 'l' or user == 'v' and bot == 's' or user == 'v' and bot == 'r' or user == 'l' and bot == 'p' or user == 'l' and bot == 'v':
            user_score+=1
        elif bot != user:
            bot_score += 1
        
    if user_score > bot_score:
        print(f"{'-'*15} Congratulation!!! {'-'*15}")
        user_win +=1
    elif bot_score > user_score:
        print(f"{'-'*15} Sorry!!! You Loser {'-'*15}")
        bot_win +=1
    else:
        print(f"{'-'*15} Draw {'-'*15}")
        draw+=1
    while True:
        exit = input("Play again [yes/no] --> ")
        if exit == 'no' or exit == 'yes':
            break
        else:
            print("\033[31m Error! Enter [yes/no] \033[0m")
    if exit == 'no':
        break

print(f'''
    User win - [{user_win}]
    Bot win  - [{bot_win}]
    Draw     - [{draw}]
''')











# 1 - Реалізувати можливість (розпочати гру знову)
# 2 - Розширити гру додавши нові варіант (ящірка, спок)
# 3 - Збільшити кількість раундів до 5-ти
# Коли користувач завершить гру (вийшов) - показати статистику по всій грі
#  User won - 2
#  Bot  won - 2
#  Draw - 2