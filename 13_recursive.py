

#5! = 5 * 4!
#4! = 4 * 3!
#3! = 3 * 2!
#2! = 2 * 1!
#1! = 1
#0! = 1

def fact(number):
    if number == 0 or number == 1:
        return 1
    return number * fact(number - 1)


# print(f"Factorial :: {fact(5)}")

# a = 1, b = 10
# 1 2 3 4 5 6 7 8 9 10

def printRange(a,b):
    print(a,end="\t")
    if a == b:
        print()
        return
    printRange(a+1,b)

printRange(1,10)


def stars(n):
    if n == 0:
        return
    print('*')
    stars(n-1)

# 12
# 321
# 3
# 2

def pal(n, result = 0):
    if n == 0:
        return result
    return pal(n//10, result * 10 + n%10)

print(pal(123))