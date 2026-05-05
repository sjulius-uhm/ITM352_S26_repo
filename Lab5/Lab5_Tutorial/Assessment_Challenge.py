# Create a Python program that:
# Stores information about books (title, author, year, genre) in dictionaries
# Creates a library (list of book dictionaries)
# Allows searching books by different criteria
# Demonstrates all major dictionary operations
# Shows nested data structures
# Samantha Julius
# Feb. 2, 2026

# Step 1: Create book dictionaries
book1 = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960,
    "genre": "Fiction"
}
book2 = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "Dystopian"
}
book3 = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genre": "Classic"
}
# Step 2: Create a library (list of book dictionaries)
library = [book1, book2, book3]

# Step 3: Function to search books by different criteria
def search_books(library, criteria, value):
    results = []
    for book in library:
        if book.get(criteria) == value:
            results.append(book)
    return results

# Step 4: Demonstrate dictionary operations
print("Library contains the following books:")
for book in library:
    print(book)
print()

# Search by author
author_search = "George Orwell"
found_books = search_books(library, "author", author_search)
print(f"Books by {author_search}:")
for book in found_books:
    print(book)
print()

# Search by genre
genre_search = "Fiction"
found_books = search_books(library, "genre", genre_search)
print(f"Books in genre {genre_search}:")
for book in found_books:
    print(book)
print()

# Demonstrate dictionary methods
sample_book = library[0]
print("Sample book dictionary methods demonstration:")
print("Keys:", list(sample_book.keys()))
print("Values:", list(sample_book.values()))
print("Items:", list(sample_book.items()))
print("Get title:", sample_book.get("title"))
sample_book.update({"year": 1961})
print("After update year:", sample_book)
removed_genre = sample_book.pop("genre")
print("After popping genre:", sample_book)
print("Removed genre:", removed_genre)
print()

# Nested data structure: Library with sections
library_with_sections = {
    "Fiction": [book1],
    "Dystopian": [book2],
    "Classic": [book3]
}
print("Library with sections:")
for section, books in library_with_sections.items():
    print(f"Section: {section}")
    for book in books:
        print(f"  {book}")
print()

# Accessing nested values
print("Accessing a book in the Fiction section:")
print(library_with_sections["Fiction"][0])

print()
# Final output
print("Final Library Structure:")
print(library_with_sections)