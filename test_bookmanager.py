import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    #Lengkapi Unit Test dibawah untuk buku yang memang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Buku tidak ada")
        self.assertFalse(removed)  
        self.assertEqual(0, self.book_manager.get_book_count())

    #Lengkapi Unit Test dibawah untuk mencari buku berdasarkan penulis
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Pemrograman", "Andi", 2020)
        book2 = Book("Jaringan Komputer", "Andi", 2021)
        book3 = Book("Basis Data", "Budi", 2022)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)

        result = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(result))  
        self.assertTrue(all(b.author == "Andi" for b in result))

    #Lengkapi Unit test dibawah untuk seluruh buku yang ada didalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Pemrograman", "Andi", 2020)
        book2 = Book("Basis Data", "Budi", 2021)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)

        result = self.book_manager.get_all_books()
        self.assertEqual(2, len(result))  
        self.assertIn(book1, result)
        self.assertIn(book2, result)

    def test_contains_existing_book(self):
        """Test cek buku yang ada"""
        book = Book("Algoritma", "Andi", 2020)
        self.book_manager.add_book(book)

        self.assertTrue(self.book_manager.contains("Algoritma"))
    
    def test_remove_with_empty_title(self):
        """Test gagal hapus buku dengan judul kosong"""
        with self.assertRaises(ValueError):
            self.book_manager.remove_book("")

    def test_find_books_by_wrong_author(self):
        """Test mencari buku dengan author salah"""
        book = Book("AI", "Budi", 2021)
        self.book_manager.add_book(book)

        result = self.book_manager.find_books_by_author("Andi")
    
        self.assertEqual(1, len(result))

    def test_year_out_of_range(self):
        """Test tambah buku dengan tahun salah"""
        
        book = Book("Masa Depan", "Citra", 2500)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())


if __name__ == "__main__":
    unittest.main()
