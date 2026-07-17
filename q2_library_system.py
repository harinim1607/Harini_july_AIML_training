catalog = {}
borrowed_books = []
members = set()

def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book borrowed successfully.")
    else:
        print("Book cannot be borrowed.")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned successfully.")
    else:
        print("Book was not borrowed.")

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id in catalog:
        if book_id not in borrowed_books:
            title, author, year = catalog[book_id]
            print(f"{book_id}: {title} by {author} ({year})")

def main():
    add_book(catalog, 1, "Python Basics", "John", 2021)
    add_book(catalog, 2, "AI Fundamentals", "Alice", 2020)
    add_book(catalog, 3, "Machine Learning", "Bob", 2022)
    add_book(catalog, 4, "Data Science", "David", 2019)

    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    return_book(borrowed_books, 1)

    show_available(catalog, borrowed_books)

main()