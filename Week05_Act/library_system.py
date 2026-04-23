class Book_jab:
    def __init__(self_jab, title_jab, author_jab, year_jab):
        self_jab.title_jab = title_jab
        self_jab.author_jab = author_jab
        self_jab.year_jab = year_jab
    
    def display_book_jab(self_jab):
        print("Title:", self_jab.title_jab)
        print("Author:", self_jab.author_jab)
        print("Year:", self_jab.year_jab)
        print()

print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_jab = Book_jab("Python Programming", "John Smith", 2022)
book2_jab = Book_jab("Data Science Basics", "Sarah Johnson", 2021)
book3_jab= Book_jab("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_jab.display_book_jab()

print("Book 2:")
book2_jab.display_book_jab()

print("Book 3:")
book3_jab.display_book_jab()
