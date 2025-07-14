
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:

# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.

# * * * * *
# *       *
# *       *
# *       * 
# * * * * *


def printSquare(length = 5, symbol = "*", fill = True):
    if fill:
        for i in range(length):
            print((symbol + " ") * length)
    else:
        for i in range(length): # 0 1 2 3 4
            if i == 0 or i == length - 1:
                print((symbol + " ") * length)
            else:
                print((symbol + " ") + " " * (length - 2)*2 + symbol)

printSquare(5,'*',False)
printSquare(10,'#',False)