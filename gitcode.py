# Simple Library Application

books = ["Science", "History", "Hannibal"]

def show_books():
    print("\nAvailable Books:")
    for b in books:
        print("-", b)

def add_book(book):
    books.append(book)
    print(book, "added successfully!")

def remove_book(book):
    if book in books:
        books.remove(book)
        print(book, "removed successfully!")
    else:
        print("Book not found!")

def search_book(book):
    if book in books:
        print(book, "is available.")
    else:
        print(book, "is not available.")


# Demo
show_books()
add_book("Prison Break")
remove_book("Hannibal")
show_books()
search_book("Science")
