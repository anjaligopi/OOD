from typing import Dict, List, Optional
import json

class Book:
    
    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return 'Title, Author, Num pages for a book: {}, {}, {}'.format(self.title, self.author, self.num_pages)

    def to_dict(self):
        dic = {}
        dic["title"] = self.title
        dic["author"] = self.author
        dic["num_pages"] = self.num_pages
        return dic

    @classmethod
    def from_dict(cls, dic): #-> Book:
        return Book(dic["title"], dic["author"], dic["num_pages"]) 

class Library: # similar to a playlist
    
    def __init__(self):
        self.books : List[Book] = []
        # self.sections

    def add_book(self, book : Book):
        self.books.append(book)

    def search_by_title(self, title : str) -> List[Book]:
        matched_books : List[Book] = []
        for book in self.books:
            if title in book.title:
                matched_books.append(book)
        return matched_books 
        
    def save_to_disk(self, file_path):
        lis_books = []
        for book in self.books:
            lis_books.append(book.to_dict())
            with open(file_path, "w") as fp:
                json.dump(lis_books, fp)

    @classmethod
    def load_from_disk(cls, file_path):
        lib_books : Library = []
        with open(file_path) as fp:
            lib = json.load(fp)
            for book_dic in lib:
                book = Book.from_dict(book_dic)
                lib_books.append(book)
                print(book)

class User:
    
    def __init__(self, uid) -> None:
        self.uid = uid
        self.curr_book : Optional[Book] = None
        self.books_list : Library = Library()
        self.curr_page : Dict[Book, int] = {}

    def read_book(self, book : Book):
        self.curr_book = book
        self.books_list.add_book(self.curr_book)
        return self.curr_page.get(self.curr_book, 0)

    def flip_page(self):
        # next page btn in UI clicked -> this func is called
        if self.curr_book not in self.curr_page:
            self.curr_page[self.curr_book] = 1
        else:
            self.curr_page[self.curr_book] += 1
        return self.curr_page


# class OnlineReaderSystem:
#     def __init__(self) -> None:
#         self.library = Library()
#         self.user = User()

def main():
    lib = Library()
    book1 = Book("Harry Potter 1", "J K Rowling", 500)
    book2 = Book("Harry Potter 2", "J K Rowling", 700)
    book3 = Book("Sherlock Holmes 1", "Sir Arthur Conan Doyle", 1500)
    book4 = Book("Sherlock Holmes 2", "Sir Arthur Conan Doyle", 900)
    lib.add_book(book1)
    lib.add_book(book2)
    user = User(1234)
    user.read_book(book3)
    user.read_book(book4)
    user.flip_page() # book4 will be the current book
    lib.save_to_disk("lib.json")
    lib2 = Library.load_from_disk("lib.json")

if __name__ == "__main__":
    main()


