import titles

class Book:

        def __init__(self, book, verse, year, auhtor):
            self.book = book
            self.year = year
            self.author = auhtor
            self.verse = verse

        def main(self):
            os.system('cls')
            titles.title()

            book = book+'.txt'
            return book

        def header(self):
            return "hello World"
            # print(self.book)

#disply options
Book.main()

## Get user input
book_verse = input("enter book ##")
verse = input("enter verse##")

# verse = Book(book_verse) 

Holy_book = Book("holy Bible", 1, 0000, "God")
Holy_verse = Book(book_verse, verse, 0000, "God")
print (Holy_book.header())

# print (Book(book_verse))
        