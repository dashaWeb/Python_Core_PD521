# number = input("Enter number :: ")
# number = int(number)
# print(f'Number :: {number}')
# print("Finally")

# while True:
#     try:
#         number = input("Enter number :: ")
#         number = int(number)    
#         print(f'Number :: {number}')
#         print("Finally block try")
#         break
#     except:
#         print("Error value (run block except)")


# print("End program")

# try:
#     test = True
#     number_1 = int(input("Enter number :: "))
#     number_2 = int(input("Enter number :: "))
#     print(f"{number_1} / {number_2} = {number_1 / number_2} {test}")
# except (TypeError, NameError):
#     print("Run block TypeError, NameError")
# except ValueError:
#     print("value error")
# except ZeroDivisionError as msg:
#     print(f"Run block ZeroDivisionError message :: {msg}")
# except Exception as msg:
#     print(f"Run block Exception message :: {msg}")
# else:
#     print("Good")
# finally:
#     print("Finally")



def printNumber(number):
    if number < 0:
        raise ValueError(f"{number} < 0 ")
    if number > 10_000:
        raise Exception(f"{number} > 10_000 ")
    print(f"Print number :: {number}")

# while True:
#     try:
#         numb = int(input("Enter number :: "))
#         printNumber(numb)
#         break
#     except ValueError as msg:
#         print(f"Block Value Error :: message :: {msg}")
#     except Exception as msg:
#         print(f"Block Exception :: message :: {msg}")

# def sum_list(list_):
#     for item in list_:
#         if item < 0:
#             raise ValueError(f"Error!!!! number is negative {item}")
#     return sum(list_)


# try:
#     print(sum_list([1,2,3,4,5,-8,10,2]))
# except Exception as msg:
#     print(msg)

numb = int(input("Enter number :: "))

print(numb)



print("Print")


