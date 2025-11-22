# Unit Testing Dasar - Python

Proyek ini merupakan implementasi **Unit Testing Dasar** menggunakan **unittest** untuk sistem manajemen buku dengan Python.

## Fitur Utama
- **Tambah Buku** ke koleksi
- **Hapus Buku** dari koleksi
- **Cari Buku** berdasarkan penulis dan tahun terbit
- **Validasi Data** buku (judul, penulis, tahun)

## Struktur Project
```text
unit-testing-python/
├── book.py
├── book_manager.py
└── test_bookmanager.py
```

## Tools dan Teknologi
- **Python 3.8+**
- **unittest** (built-in testing framework)

## Cara Menjalankan Unit Test
1. Pastikan **Python 3.8+** sudah terinstal.
2. Clone repository:
```bash
git clone [URL_REPOSITORY]
cd unit-testing-python
```
3. Jalankan test:
```bash
python -m unittest test_bookmanager.py -v
```
4. Atau jalankan dengan discovery:
```bash
python -m unittest discover -s . -p "test_*.py"
```

## Test Cases
- ✅ Tambah buku ke koleksi
- ✅ Hapus buku yang ada
- ✅ Hapus buku yang tidak ada
- ✅ Cari buku berdasarkan penulis
- ✅ Ambil semua buku
- ✅ Cek keberadaan buku
- ✅ Validasi tahun terbit (2000-2100)
- ✅ Error handling untuk input invalid

## Catatan
- Tahun terbit harus antara **2000-2100**
- Judul dan penulis **tidak boleh kosong** atau hanya spasi
- Test menggunakan `setUp()` untuk inisialisasi sebelum setiap test
- Gunakan `assertRaises()` untuk test exception

---
**Politeknik Negeri Cilacap** - Modul Praktikum 1: Unit Testing Dasar
