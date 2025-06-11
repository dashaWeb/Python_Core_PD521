'''
    > 
    <
    >=
    <=
    ==
    !=

'''

a = 7
b = 7


print(f"{a} > {b} --> {a>b}")  # False
print(f"{a} < {b} --> {a<b}")  # True
print(f"{a} >= {b} --> {a>=b}")  # False
print(f"{a} <= {b} --> {a<=b}")  # True
print(f"{a} == {b} --> {a==b}")  # True

password = "mka5"
print(f"{password} != mka5 --> {password != 'mka5'}") # False

login = "mka"
print("="*100)
print(f"{password} == mka5 --> {password == 'step'}") # True
print(f"{login} == mka --> {login == 'mka'}") # True

# and 
# or 

print(f"password == 'step' and login == 'mka' {password == 'step' and login == 'mka'}") # False
print(f"password == 'mka5' and login == 'mka' {password == 'mka5' and login == 'mka'}") # True

# month = int(input("Enter month --> "))
# print(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 1)

# year = int(input("Enter year --> "))

# days = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) + 365
# print(days)

# login = "test2"
# if password == 'mka5' and login == 'mka':
#     print("Welcome")
#     print("="*50)
# else:
#     print("Error")


# day = int(input("Enter numbe day --> "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error")


# print("-----------------")


# number = int(input("Enter number "))
# if number >= 0 and number <= 20:
#     print("belongs to the range")
# elif number > 20 or number < 0:
#     print("does not belong to the range")


login = input("Enter login :: ")
if login == "cancel":
    print("login canceled")
elif login == "admin" or login == "Admin" or login == "ADMIN":
    password = input("Enter password :: ")
    if password == "cancel":
        print("login canceled")
    elif password == "step":
        print("Welcome")
    else:
        print("Error password")
else:
    print("i don't know you")

