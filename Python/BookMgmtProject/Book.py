class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Publish: {self.publication_year}"
    

class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)


    def display_all_books(self):
        if self.books == None:
            print("Library is empty...")

        for i in range(len(self.books)):
            print(self.books[i])


    def search_book_by_title(self, title):
        self.sort_books_by_title()

        # binary search
        left = 0
        right = len(self.books) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_title = self.books[mid].title.lower()

            if mid_title == title.lower():
                return self.books[mid]
            elif mid_title < title.lower():
                left = mid + 1
            else:
                right = mid - 1
        return None
    

    def sort_books_by_title(self):
        n = len(self.books)

        # bubble sort
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.books[j].title.lower() > self.books[j + 1].title.lower():
                    self.books[j], self.books[j + 1] = self.books[j + 1], self.books[j]





def main():
    mikesLibrary = Library()

    for i in range(5):
        bName = input("Enter book name: ")
        bAuthor = input("Enter author name: ")
        bISBN = input("Enter the ISBN: ")
        bPubl = input("Enter the year the book was published: ")
        print()
        
        mikesLibrary.add_book(Book(bName, bAuthor, bISBN, bPubl))


    mikesLibrary.display_all_books()
    mikesLibrary.sort_books_by_title()
    print()
    mikesLibrary.display_all_books()


    while True:
        print("\nLibrary Menu:")
        print("1. Display all books")
        print("2. Sort books by title")
        print("3. Search for a book by title")
        print("4. Exit\n")

        choice = int(input("enter a number 1 thru 4: "))

        if choice == 1:
            mikesLibrary.display_all_books()
            print()
        elif choice == 2:
            mikesLibrary.sort_books_by_title()
            print("sorting complete\n")
        elif choice == 3:
            user_search = input("enter book title to search: ")
            found_title = mikesLibrary.search_book_by_title(user_search)

            if found_title:
                print("\nFound: ", found_title)
            else:
                print("\nTitle not found")
        elif choice == 4:
            print("Goodbye...")
            break
        else:
            print("invalid entry, enter a number between 1 and 4.")


if __name__ == '__main__':
    main()