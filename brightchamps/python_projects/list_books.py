books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'year': 1932},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
]


def filter_books(title=None):
    filtered_books = books
    
    if title:
        filtered_books = filter(lambda book: title.lower() in book['title'].lower(), filtered_books)
        
    # if author:
    #     filtered_books = filter(lambda book: author.lower() in book['author'].lower(), filtered_books)
        
    # if year:
    #     filtered_books = filter(lambda book: book['year'] == year, filtered_books)
        
    return list(filtered_books)

title = input("\nBook title: ")
# author = input("Author: ")
# year = input("Year: ")
filtered_books = filter_books(title)

print(filtered_books,"\n")
