class Book:
    page_material = "бумага"
    have_text = True

    def __init__(self, name, author, pages_number, isbn=None):
        self.name = name
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.reserved = False

    def to_dict(self):
        return {
            "Название": self.name,
            "Автор": self.author,
            "страниц": self.pages_number,
            "материал": self.page_material
        }

    def print_result(self):
        info = self.to_dict()

        parts = [f"{key}: {value}" for key, value in info.items()]
        result = ", ".join(parts)

        if self.reserved:
            result += ", зарезервирована"

        print(result)


class SchoolBook(Book):

    def __init__(self, name, author, pages_number, subject, school_class, tasks=False):
        super().__init__(name, author, pages_number)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def to_dict(self):
        return {
            "Название": self.name,
            "Автор": self.author,
            "страниц": self.pages_number,
            "предмет": self.subject,
            "класс": self.school_class
        }


classic_book = Book("Идиот", "Достоевский", 500)
classic_book.reserved = True

fantasy_book = Book("The Hobbit", "Tolkien", 300)
biography_book = Book("Becoming", "Obama", 400)
horror_book = Book("The Shining", "King", 800)
poetry_book = Book("Стихотворения и поэмы", "Есенин", 250)

math_book = SchoolBook("Алгебра", "Иванов", 200, "Математика", 9)
math_book.reserved = True

russian = SchoolBook("Русский язык", "Баранов", 200, "Русский язык", 7)
physics = SchoolBook("Физика", "Перышкин", 200, "Физика", 8)

classic_book.print_result()
fantasy_book.print_result()
biography_book.print_result()
horror_book.print_result()
poetry_book.print_result()

math_book.print_result()
russian.print_result()
physics.print_result()
