import json
directory = '18_file'

file_t = 'file.txt'
file_b = 'file.dat'
file_j = 'file.json'

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In volutpat faucibus scelerisque. Vestibulum fringilla nunc vitae porta lobortis. Vestibulum tincidunt vestibulum tellus eget molestie. Donec molestie diam est, at blandit mi laoreet eu. Aliquam ultrices quam vel leo placerat auctor. Praesent pulvinar nisi eget orci lacinia molestie. Sed gravida leo quis tortor feugiat, vel consequat eros ornare. Morbi pretium et nisl sit amet auctor."

list_ = ["red", "green", "blue", "yellow", "purple", "pink"]

dict_ = {'name': 'table', 'width': 500, 'height': 300, 'align': 'center'}

group = [
    {
        "name": "Austen",
        "last_name": "Maudlin",
        "email": "amaudlin0@oaic.gov.au",
        "date": "19/11/2000"
    }, {
        "name": "Elonore",
        "last_name": "Francke",
        "email": "efrancke1@google.com.br",
        "date": "28/11/2008"
    }, {
        "name": "Tova",
        "last_name": "Carberry",
        "email": "tcarberry2@newsvine.com",
        "date": "02/01/2002"
    }, {
        "name": "Jobye",
        "last_name": "Archbell",
        "email": "jarchbell3@usa.gov",
        "date": "10/07/2007"
    }, {
        "name": "Ddene",
        "last_name": "Agirre",
        "email": "dagirre4@scientificamerican.com",
        "date": "02/01/2010"
    }, {
        "name": "Audre",
        "last_name": "Arnke",
        "email": "aarnke5@uiuc.edu",
        "date": "08/03/2009"
    }, {
        "name": "Frieda",
        "last_name": "O'Tierney",
        "email": "fotierney6@nasa.gov",
        "date": "21/02/2005"
    }, {
        "name": "Rhona",
        "last_name": "Crombleholme",
        "email": "rcrombleholme7@boston.com",
        "date": "18/01/2005"
    }, {
        "name": "Orlan",
        "last_name": "Platt",
        "email": "oplatt8@eepurl.com",
        "date": "29/05/2007"
    }, {
        "name": "Delainey",
        "last_name": "Reding",
        "email": "dreding9@nps.gov",
        "date": "03/09/2005"
    }]


# with open(f'{directory}/{file_t}', 'w') as file:
#     file.write(line)

# with open(f'{directory}/{file_t}', 'r') as file:
#     print(file.read())


# with open(f'{directory}/{file_t}', 'w') as file:
#     file.writelines(list_)

# with open(f'{directory}/{file_t}', 'r') as file:
#     print(file.readlines())

# with open(f'{directory}/{file_t}', 'w') as file:
#     file.writelines(dict_)

# with open(f'{directory}/{file_t}', 'w') as file:
#     file.write(group)

# import pickle

# with open(f'{directory}/{file_t}', 'w') as file:
#     file.write(line)

# with open(f'{directory}/{file_b}','wb') as file:
#     # res = pickle.dumps(line)
#     # print(type(res), res)
#     # file.write(res)
#     pickle.dump(line,file)

# with open(f'{directory}/{file_b}','rb') as file:
#     # text_b  = file.read()
#     # print(pickle.loads(text_b))
#     print(pickle.load(file))

# with open(f'{directory}/{file_b}','wb') as file:
#     pickle.dump(list_,file)


# with open(f'{directory}/{file_b}','rb') as file:
#     res = pickle.load(file)

# for color in res:
#     print(color)

# with open(f'{directory}/{file_b}','wb') as file:
#     pickle.dump(dict_,file)


# with open(f'{directory}/{file_b}','rb') as file:
#     res = pickle.load(file)
#     print(res)

# with open(f'{directory}/{file_b}','wb') as file:
#     pickle.dump(group,file)


# with open(f'{directory}/{file_b}','rb') as file:
#     res = pickle.load(file)
#     print(res)

# def printStud(group):
#     for stud in group:
#         for key, val in stud.items():
#             print(key, ":", val)
#         print()

# printStud(res)

# new_stud = {
#         "name": "Audre33333",
#         "last_name": "Arnke33333",
#         "email": "aarnke5@uiuc.edu3333",
#         "date": "08/03/20093333"
#     }

# res.append(new_stud)
# print(res)
# with open(f'{directory}/{file_b}','wb') as file:
#     pickle.dump(res,file)

# with open(f'{directory}/{file_b}','rb') as file:
#     res = pickle.load(file)


# printStud(res)

# with open(f'{directory}/{file_j}', 'w') as file:
#     print(json.dumps(group))
#     file.write(json.dumps(group))

# with open(f'{directory}/{file_j}', 'r') as file:
#     res = file.read()
#     res = json.loads(res)


# def printStud(group):
#     for stud in group:
#         for key, val in stud.items():
#             print(key, ":", val)
#         print()


# # with open(f'{directory}/{file_j}', 'w') as file:
# #     json.dump(group,file)
# with open(f'{directory}/{file_j}', 'r') as file:
#     res = json.load(file)
# printStud(res)


import requests

res = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
currency = json.loads(res.content)
while True:
    choise = input('''
        1 - EUR - UAH
        2 - UAH - EUR 
        3 - USD - UAH
        4 - UAH - USD 
        0 - exit
        ''')
    money = int(input('Enter number of :: '))
    match choise:
        case '1':
            print(f'Result :: {money * float(currency[0]["buy"])}')
        case '2':
            print(f'Result :: {money / float(currency[0]["sale"])}')
    if choise == '0':
        break