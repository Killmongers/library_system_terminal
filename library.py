import json
import os

data_file = "library.json"

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(data_file):
            with open(data_file, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_books(self):
        with open(data_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author,
            "available": True,
            "borrowed_by": None
        }
        self.books.append(book)
        self.save_books()

    def view_books(self):
        if not self.books:
            print("No books in library yet.")
        else:
            for i, book in enumerate(self.books, start=1):
                status = "Available" if book["available"] else f"Borrowed by {book['borrowed_by']}"
                print(f"{i}. {book['title']} by {book['author']} - {status}")

    def borrow_book(self, book_number, member_name):
        index = book_number - 1
        if 0 <= index < len(self.books):
            if self.books[index]["available"]:
                self.books[index]["available"] = False
                self.books[index]["borrowed_by"] = member_name
                self.save_books()
                print(f"{member_name} borrowed '{self.books[index]['title']}'")
            else:
                print("The book is already borrowed.")
        else:
            print("Invalid book number.")

    def return_book(self, book_number):
        index = book_number - 1
        if 0 <= index < len(self.books):
            if not self.books[index]["available"]:
                borrower = self.books[index]["borrowed_by"]
                self.books[index]["available"] = True
                self.books[index]["borrowed_by"] = None
                self.save_books()
                print(f"{borrower} returned '{self.books[index]['title']}'")
            else:
                print("This book is already available.")
        else:
            print("Invalid book number.")


lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. View all books")
    print("2. Add a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        lib.view_books()
    elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        lib.add_book(title, author)
        print("Book added.")
    elif choice == "3":
        lib.view_books()
        try:
            book_num = int(input("Enter book number to borrow: "))
            member_name=input("Enter your name: ")
            lib.borrow_book(book_num,member_name)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        lib.view_books()
        try:
            book_num = int(input("Enter book number to return: "))
            lib.return_book(book_num)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
