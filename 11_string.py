word = "Length"

print(word[2])
# word[2] = 'd' #Error

# for char in word:
#     print(ord(char))

# for i in range(32,256):
#     print(chr(i), end="\t")
#     if i% 15 == 0:
#         print()


# print("{0} Login :: {0}{1} \nPassword :: {1}".format("Admin","qwerty123"))

# line = "Lorem ipsum dolor sit amet"
# length = len(line)
# print(f'Length line :: {length}')
# print(f'last char :: {line[len(line) - 1]}')
# print(f'last char :: {line[- 1]}')

# # [start:stop:step]
# print(line[-1:6:-1])
# print(line[:20])
# print(line[::2])
# print(line[::-1])


# numbers = "123456789"
# letters = "alksjdfg"
line = "Lorem ipsum dolor sit"
# word = "Fruit Apple"
# word_2 = "BANANA"
# letterDig = "hgjgjg112545ggg"
# symbols = "-=)$%$^&"

# перевірка лише букв або цифр
# print("\n=================== numbers.isalnum() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.isalnum()}")
# print(f"\t {letters} \t\t --------> \t {letters.isalnum()}")
# print(f"\t {line} \t --------> \t {line.isalnum()}")
# print(f"\t {word} \t\t --------> \t {word.isalnum()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.isalnum()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.isalnum()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.isalnum()}")
# print("================================================================")


# # лише букви
# print("\n=================== numbers.isalpha() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.isalpha()}")
# print(f"\t {letters} \t\t --------> \t {letters.isalpha()}")
# print(f"\t {line} \t --------> \t {line.isalpha()}")
# print(f"\t {word} \t\t --------> \t {word.isalpha()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.isalpha()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.isalpha()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.isalpha()}")
# print("================================================================")

# # лише цифри
# print("\n=================== numbers.isdigit() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.isdigit()}")
# print(f"\t {letters} \t\t --------> \t {letters.isdigit()}")
# print(f"\t {line} \t --------> \t {line.isdigit()}")
# print(f"\t {word} \t\t --------> \t {word.isdigit()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.isdigit()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.isdigit()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.isdigit()}")
# print("================================================================")

# # лише пропуски
# # letters = '      '
# print("\n=================== numbers.isspace() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.isspace()}")
# print(f"\t {letters} \t\t --------> \t {letters.isspace()}")
# print(f"\t {line} \t --------> \t {line.isspace()}")
# print(f"\t {word} \t\t --------> \t {word.isspace()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.isspace()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.isspace()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.isspace()}")
# print("================================================================")


# # перевірка букв на нижній регістр
# print("\n=================== numbers.islower() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.islower()}")
# print(f"\t {letters} \t\t --------> \t {letters.islower()}")
# print(f"\t {line} \t --------> \t {line.islower()}")
# print(f"\t {word} \t\t --------> \t {word.islower()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.islower()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.islower()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.islower()}")
# print("================================================================")

# # перевірка букв на верхній регістр
# print("\n=================== numbers.isupper() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.isupper()}")
# print(f"\t {letters} \t\t --------> \t {letters.isupper()}")
# print(f"\t {line} \t --------> \t {line.isupper()}")
# print(f"\t {word} \t\t --------> \t {word.isupper()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.isupper()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.isupper()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.isupper()}")
# print("================================================================")

# # перші букви у слові на верхній регістр
# print("\n=================== numbers.istitle() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.istitle()}")
# print(f"\t {letters} \t\t --------> \t {letters.istitle()}")
# print(f"\t {line} \t --------> \t {line.istitle()}")
# print(f"\t {word} \t\t --------> \t {word.istitle()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.istitle()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.istitle()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.istitle()}")
# print("================================================================")


# print("\n=================== numbers.lower() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.lower()}")
# print(f"\t {letters} \t\t --------> \t {letters.lower()}")
# print(f"\t {line} \t --------> \t {line.lower()}")
# print(f"\t {word} \t\t --------> \t {word.lower()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.lower()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.lower()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.lower()}")
# print("================================================================")

# print("\n=================== numbers.upper() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.upper()}")
# print(f"\t {letters} \t\t --------> \t {letters.upper()}")
# print(f"\t {line} \t --------> \t {line.upper()}")
# print(f"\t {word} \t\t --------> \t {word.upper()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.upper()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.upper()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.upper()}")
# print("================================================================")


# print("\n=================== numbers.capitalize() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.capitalize()}")
# print(f"\t {letters} \t\t --------> \t {letters.capitalize()}")
# print(f"\t {line} \t --------> \t {line.capitalize()}")
# print(f"\t {word} \t\t --------> \t {word.capitalize()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.capitalize()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.capitalize()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.capitalize()}")
# print("================================================================")

# print("\n=================== numbers.title() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.title()}")
# print(f"\t {letters} \t\t --------> \t {letters.title()}")
# print(f"\t {line} \t --------> \t {line.title()}")
# print(f"\t {word} \t\t --------> \t {word.title()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.title()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.title()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.title()}")
# print("================================================================")

# print("\n=================== numbers.swapcase() =======================")
# print(f"\t {numbers} \t\t --------> \t {numbers.swapcase()}")
# print(f"\t {letters} \t\t --------> \t {letters.swapcase()}")
# print(f"\t {line} \t --------> \t {line.swapcase()}")
# print(f"\t {word} \t\t --------> \t {word.swapcase()}")
# print(f"\t {word_2} \t\t --------> \t {word_2.swapcase()}")
# print(f"\t {letterDig} \t --------> \t {letterDig.swapcase()}")
# print(f"\t {symbols} \t\t --------> \t {symbols.swapcase()}")
# print("================================================================")


# line += " " + line + " ipsum"
# print(line)

# print("\n=================== line.find() =======================")
# print(f"{line} \t --------> \t {line.find('ipsum')}")
# print(f"{line} \t --------> \t {line.find('ipsum',7)}")
# print(f"{line} \t --------> \t {line.find('ipsum',29)}")
# print(f"{line} \t --------> \t {line.find('ipsum',45)}")


# print("\n=================== line.find() =======================")
# index = -1
# while True:
#     index = line.find("ipsum", index + 1)
#     if index == -1:
#         break
#     print(f"{line} \t --------> \t {index}")


# print("\n=================== line.rfind() =======================")
# print(f"{line} \t --------> \t {line.rfind('ipsum')}")
# print(f"{line} \t --------> \t {line.rfind('ipsum',0,44)}")
# print(f"{line} \t --------> \t {line.rfind('ipsum',0,28)}")
# print(f"{line} \t --------> \t {line.rfind('ipsum',0,6)}")


# print("\n=================== line.index() =======================")
# print(f"{line} \t --------> \t {line.index('ipsum')}")
# print(f"{line} \t --------> \t {line.index('ipsum',7)}")
# print(f"{line} \t --------> \t {line.index('ipsum',29)}")
# # print(f"{line} \t --------> \t {line.index('ipsum',45)}") #ValueError

# print("\n=================== line.rindex() =======================")
# print(f"{line} \t --------> \t {line.rindex('ipsum')}")


# print("\n=================== line.count() =======================")
# print(f"{line} \t --------> \t Count ::  {line.count('ipsum')}")


# print("\n=================== line.count() =======================")
# print(f"{line} \t --------> \t Count ::  {line.replace('ipsum','yellow',2)}")

# import re

# str_1 = "123"
# str_2 = "234"
# str_3 = "Lorem** 21 ipsum red"
# print("\n=================== re.search('template', str) =======================")
# print(f"{str_1} \t --------> \t {re.search('12',str_1)}")
# print(f"{str_2} \t --------> \t {re.search('12',str_2)}")
# print(f"{str_3} \t --------> \t {re.search('12',str_3)}")

# print("\n=================== re.search('template', str) =======================")
# print(f"{str_1} \t --------> \t {re.search('[12abcd]',str_1)}")
# print(f"{str_2} \t --------> \t {re.search('[12abcd]',str_2)}")
# print(f"{str_3} \t --------> \t {re.search('[12abcd]',str_3)}")

# print("\n=================== re.search('template', str) =======================")
# print(f"{str_1} \t --------> \t {re.search('[0-9]',str_1)}")
# print(f"{str_2} \t --------> \t {re.search('[0-9]',str_2)}")
# print(f"{str_3} \t --------> \t {re.search('[0-9]',str_3)}")

# print("\n=================== re.search('template', str) =======================")
# print(f"{str_1} \t --------> \t {re.search('[a-zA-Z]',str_1)}")
# print(f"{str_2} \t --------> \t {re.search('[a-zA-Z]',str_2)}")
# print(f"{str_3} \t --------> \t {re.search('[a-zA-Z]',str_3)}")

# match = re.search('[a-zA-Z]',str_3)
# if match:
#     print("Find by letter")
# else:
#     print("not found letter")


# print(f"{str_3} \t --------> \t {re.search('[^a-zA-Z* ]',str_3)}")
# print(f"{str_3} \t --------> \t {re.search(r'^[a-zA-Z]{5}[*]*',str_3).group(0)}")
# template = "\w"
# print(str_3," \t --------> \t",re.search("\w+",str_3))
# print(str_3," \t --------> \t",re.findall("\w+",str_3))
# print(str_3," \t --------> \t",re.findall("\W+",str_3))

# print(str_3," \t --------> \t",re.sub("\w{3}$", 'yellow',str_3))

# str_3 += " 04/02/2000"
# print(str_3," \t --------> \t",re.search("\d{1,2}\/\d{1,2}\/\d{4}",str_3))


# import string
# import random
# print('Lorem'.center(50))
# print('Lorem'.center(50,'*'))
# print('\tLorem\t  rr'.expandtabs(10))
# print('Lorem'.rjust(30,'*'))
# print('Lorem'.ljust(30,'='))
# print('Lomrem'.lstrip('Lo'))
# print('Lomrem'.rstrip('m'))
# print('mLomrmem'.strip('m'))
# print('L124'.zfill(10))

# print("ttest {0:3.2f}".format(2.36589))
# print("ttest {0:4d}".format(20))
# print("ttest {0:^10}".format(20))
# print("ttest {0:>10}".format(20))
# print("ttest {0:<10}!!!".format(20))

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# userLogin = ''.join(random.sample((string.ascii_lowercase),6))
# userPass = ''.join(random.sample((string.ascii_letters+string.digits+string.punctuation),8))
# print(userLogin)
# print(userPass)

line = input("Enter string :: ")
old = input("Enter :: ")
new_ = input("Enter :: ")

print(f"{line} \t --------> \t Count ::  {line.replace(old,new_)}")