class Book:
    def __init__(self, title, author, available = True ):
        self.title = title
        self.author = author
        self.available = available

    def checking_out(self):

        if self.available:
            self.available = False
            print(f"Book '{self.title}' by '{self.author}' is not avaiable")


    def return_book(self):
        if not self.available:
            self.available = Ture
            print(f"Book '{self.title}' by '{self.author}' has been returned")

class BookDB:

    def __init__(self):
        self.catalog = [] # self.catalog is a list of "Book" objects

    def add_book(self, book):
        self.catalog.append(book)
        print(f" The book '{book.title}' has been added to the book database.")


    def display_catalog(self):
        print("Library Catalog:")
        for book in self.catalog:
            # define a string variable called status and assign it as "available" if book.available = Ture
            status = "Available" if book.available else "Checked Out"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")


def main():
    book_db = BookDB()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book_db.add_book(book1)
    book_db.add_book(book2)


    while True:
        print("\nPlease entry your selection:")
        print("1: Add a new book, 2: Display book catalog, 3: Checking out a book   4: Return a book    0:Exit" )

        choice = input("Choose an option (1/2/3/4/0): ")

        if choice == '1':
            title = input("Enter the title of the new book: ")
            author = input("Enter the author of the new book: ")
            new_book = Book(title, author)

            book_db.add_book(new_book)

        elif choice == '2':
            book_db.display_catalog()

        elif choice == '3':
            title = input("Enter the title of the book to check out: ")

            for book in book_db.catalog:
                if book.title.lower() == title.lower():
                    book.checkout()
                    break
            else:
                print("Book not found in the catalog.")

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            for book in book_db.catalog:
                if book.title.lower() == title.lower():
                    book.return_book()
                    break
                else:
                    print("Book is not found in the catalog")

        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
