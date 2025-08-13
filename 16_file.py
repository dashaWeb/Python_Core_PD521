# open
# read
# write
# close

# "C:\Users\konopelko\Desktop\main.css" -- absolute 
# "../main.css" -- relative
# handler = open("16_file/text.txt")
# print(handler.read())
# handler.close()

# print("=" * 50)
# handler = open("16_file/text.txt")
# print(handler.read(5))
# handler.seek(0)
# print(handler.read(5))

# handler.close()


# url = r"C:\Users\konopelko\Desktop\1904217.webp"

# handler = open(url,'rb')
# print(handler.read())


url = r"16_file/text.txt"

# handler = open(url)
# print(handler.readline())
# print("=" * 50)
# print(handler.readline())
# handler.seek(0)

# print("=" * 50)
# for line in handler:
#     print(line)

# handler.seek(0)
# print(handler.readlines())

# handler.close()

# try:
#     handler = open(url)
#     print(int(handler.read()))
# except FileNotFoundError as msg:
#     print(msg)
# except Exception as msg:
#     print(msg)
# finally:
#     handler.close()


# with open(url) as handler:
#     print(handler.read())


# with open("16_file/test_write.txt", "w") as handler:
#     handler.write("Test line 2")


# with open("16_file/test_write.txt", "a") as handler:
#     handler.write("Test line 3\n")


# with open("16_file/test_write.txt", "w") as handler:
#     handler.writelines(["line 1 \n", "line 2 \n", "line 3 \n"])

# line = "Сніг, Дощ, Хмара, Сонце"
# with open("16_file/test_write.txt", "w", encoding='utf-8') as handler:
#     handler.write(line)

with open("16_file/test_write.txt", "r", encoding="utf-8") as handler:
    print(handler.read())







