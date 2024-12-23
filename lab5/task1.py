class Book:

    title = "Четвертое крыло"
    author = "Ребекка Яррос"
    year = 2023

    def get_info(self):
        print("Название книги: {}, Автор: {}, Год издания: {}".format(self.__class__.title,self.__class__.author,self.__class__.year))
    
book = Book()
book.get_info()
print(Book.year)