from library import Library

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
