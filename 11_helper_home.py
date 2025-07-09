# Завдання 3
# Користувач вводить з клавіатури деякий текст. У програмі визначено набір зарезервованих слів. Необхідно знайти в тексті всі зарезервовані слова і змінити їхній регістр на верхній. Вивести на екран змінений текст.

# text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean rutrum sem ut interdum volutpat. Mauris elementum elit sapien, nec efficitur leo tempor nec. Etiam semper elit maximus, ornare nisl sed, luctus metus. Nullam sollicitudin convallis ex, ut tincidunt ligula pulvinar in. Maecenas fringilla scelerisque nunc et sodales. Etiam at orci tortor. Etiam molestie at quam at tincidunt. Aliquam tincidunt elit et placerat sagittis. Phasellus sagittis sollicitudin tincidunt. Fusce ac dictum nisl. Nunc sed nisl non arcu pellentesque scelerisque eu a nunc. Ut metus dui, rutrum id venenatis eget, consequat vitae turpis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae'''
# control = ["ipsum","nec","tincidunt","elit"]

# print(text)
# print()
# for word in control:
#     text = text.replace(word, word.upper())
# print(text)


# Завдання 5
# Користувач вводить текст і набір символів. Видаліть з тексту всі слова, що містять хоча б один з цих символів, і виведіть результат.

import re
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean rutrum sem ut interdum volutpat. Mauris elementum elit sapien, nec efficitur leo tempor nec. Etiam semper elit maximus, ornare nisl sed, luctus metus. Nullam sollicitudin convallis ex, ut tincidunt ligula pulvinar in. Maecenas fringilla scelerisque nunc et sodales. Etiam at orci tortor. Etiam molestie at quam at tincidunt. Aliquam tincidunt elit et placerat sagittis. Phasellus sagittis sollicitudin tincidunt. Fusce ac dictum nisl. Nunc sed nisl non arcu pellentesque scelerisque eu a nunc. Ut metus dui, rutrum id venenatis eget, consequat vitae turpis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae'''
# symbols = 's o l r'.split(" ")
# print(symbols)

# words = re.findall('[ ]*\w+[ .,!]', text)
# print(words)

# for s in symbols:
#     for word in words:
#         index = word.lower().find(s)
#         if index != -1:
#             text = text.replace(word,"")
# print(text)
