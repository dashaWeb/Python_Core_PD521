books = [
    {
        'title':'title_1',
        'author':'author_1',
        'publisher':'publisher_1',
        'price':145,
        'rating':9
    },
    {
        'title':'title_2',
        'author':'author_2',
        'publisher':'publisher_2',
        'price':250,
        'rating':7
    },
    {
        'title':'title_3',
        'author':'author_3',
        'publisher':'publisher_3',
        'price':505,
        'rating':5
    }
]

def printBook(book, number = None):
    if number:
        print(f'Book #{number}'.center(50,'-'))
    print(f'\t Title     :: {book["title"]}')
    print(f'\t Author    :: {book["author"]}')
    print(f'\t Publisher :: {book["publisher"]}')
    print(f'\t Price     :: {book["price"]}')
    print(f'\t Rating    :: {book["rating"]}')
    print()

def printAllBooks(books):
    i = 1
    for book in books:
        printBook(book,i)
        i+=1

def editBook(book):
    book['title'] = input("Enter title book :: ")
    book['author'] = input("Enter author book :: ")
    book['publisher'] = input("Enter publisher book :: ")
    book['price'] = float(input("Enter price book :: "))
    book['rating'] = float(input("Enter rating book :: "))

def find_by_author(author):
    return list(filter(lambda x : x['author'].upper() == author.upper(), books))
id = 1
printAllBooks(books)
editBook(books[id-1])
printAllBooks(books)
author = '1'

printAllBooks(find_by_author('author_2'))