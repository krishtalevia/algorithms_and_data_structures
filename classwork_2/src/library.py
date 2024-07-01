class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        if book not in self.__books:
            self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            for i in range(0, len(self.__books), 1):
                if self.__books[i] == book:
                    del self.__books[i]
                    return

    def find_book(self, book):
        if book in self.__books:
            return True
        else:
            False

# Легаси код для тестов
import unittest

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.assertFalse(self.library.find_book("Book B"))

    def test_remove_book(self):
        self.library.add_book("Book A")
        self.library.add_book("Book B")
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))
        self.library.remove_book("Book B")
        self.assertFalse(self.library.find_book("Book B"))
        self.library.remove_book("Book B")

    def test_find_book(self):
        self.library.add_book("Book A")
        self.assertTrue(self.library.find_book("Book A"))
        self.library.remove_book("Book A")
        self.assertFalse(self.library.find_book("Book A"))

if __name__ == '__main__':
    unittest.main()
