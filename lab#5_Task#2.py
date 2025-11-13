
library_db = {
    "The Great Gatsby": ("F. Scott Fitzgerald","Action", 1925,"YES"),
    "To Kill a Mockingbird": ("Harper Lee","Romance" ,1960,"NO"),
    "1984": ("George Orwell","Science Fiction", 1949,"YES"),
    "Pride and Prejudice": ("Jane Austen","Romance", 1813,"YES"),
    "The Catcher in the Rye": ("J.D. Salinger","Fiction", 1951,"NO")
}
def add_book(title, author, genre, year,availability):
    if title in library_db:
        return "Book already exists in the database."
    library_db[title] = (author, genre, year,availability)
    return "Book added successfully."

def remove_book(title):
    if title in library_db:
        del library_db[title]
        return "Book removed successfully."
    return "Book not found in the database."

def update_book(title, author=None, genre=None, year=None, availability=None):
    if title not in library_db:
        return "Book not found in the database."
    current_author, current_genre, current_year, current_availability = library_db[title]
    library_db[title] = (
        author if author is not None else current_author,
        genre if genre is not None else current_genre,
        year if year is not None else current_year,
        availability if availability is not None else current_availability
    )
    return "Book updated successfully."

def display_books():
    for title, (author, genre, year, availability) in library_db.items():
        print(f"Title: {title}, Author: {author}, Genre: {genre}, Year: {year}, Availability: {availability}")

def search_by_title(title):
    return library_db.get(title, "Book not found in the database.")

def search_by_author(author):
    results = {title: details for title, details in library_db.items() if details[0] == author}
    return results if results else "No books found by this author."
def search_by_genre(genre):
    results = {title: details for title, details in library_db.items() if details[1] == genre}
    return results if results else "No books found in this genre."

def borrow_return_book(title, action):
    if title not in library_db:
        return "Book not found in the database."
    author, genre, year, availability = library_db[title]
    if action == "borrow":
        if availability == "YES":
            library_db[title] = (author, genre, year, "NO")
            return f"You have borrowed '{title}'."
        else:
            return f"'{title}' is currently not available."
    elif action == "return":
        if availability == "NO":
            library_db[title] = (author, genre, year, "YES")
            return f"You have returned '{title}'."
        else:
            return f"'{title}' was not borrowed."
    else:
        return "Invalid action. Use 'borrow' or 'return'."
    
def loopfunction():
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Update Book Information")
        print("4. Display Books")
        print("5. Search by Title")
        print("6. Search by Author")
        print("7. Search by Genre")
        print("8. Borrow or Return Book")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = int(input("Enter publication year: "))
            availability = input("Is the book available? (YES/NO): ").upper()
            print(add_book(title, author, genre, year, availability))
        elif choice == '2':
            title = input("Enter book title to remove: ")
            print(remove_book(title))
        elif choice == '3':
            title = input("Enter book title to update: ")
            author = input("Enter new author (leave blank to keep current): ") or None
            genre = input("Enter new genre (leave blank to keep current): ") or None
            year = input("Enter new publication year (leave blank to keep current): ") or None
            year = int(year) if year else None
            availability = input("Is the book available? (YES/NO, leave blank to keep current): ").upper() or None
            print(update_book(title, author, genre, year, availability))
        elif choice == '4':
            display_books()
        elif choice == '5':
            title = input("Enter book title to search: ")
            print(search_by_title(title))
        elif choice == '6':
            author = input("Enter author to search: ")
            print(search_by_author(author))
        elif choice == '7':
            genre = input("Enter genre to search: ")
            print(search_by_genre(genre))
        elif choice == '8':
            title = input("Enter book title: ")
            action = input("Enter action (borrow/return): ").lower()
            print(borrow_return_book(title, action))
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

loopfunction()  

