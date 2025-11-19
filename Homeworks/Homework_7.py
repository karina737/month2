import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
                 )
                 """)
    
def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)""",
    (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

if __name__=='__main__':
    conn = sqlite3.connect('database.db')
    create_table(conn)
    insert_books(conn, 'Анна Каренина', 'Л. Толстой', 1877, 'Роман', 850, 3)
    insert_books(conn, 'Гордость и предубеждение', 'Д. Остин', 1813, 'Роман', 400, 1)
    insert_books(conn, 'Мастер и Маргарита', 'М. Булгаков', 1967, 'Сатира/Роман', 500, 2)
    insert_books(conn, 'Преступление и наказание', 'Ф. Достоевский', 1866, 'Психологический роман', 550, 6)
    insert_books(conn, 'Война и мир', 'Л. Тодстой', 1869, 'Исторический роман', 1500, 2)
    insert_books(conn, 'Код да Винчи', 'Д. Браун', 2003, 'Детектив', 544, 1)
    insert_books(conn, 'Мертвые души', 'Н. Гоголь', 1842, 'Поэма', 352, 3)
    insert_books(conn, 'Евгений Онегин', 'А. Пушкин', 1833, 'Роман в стихах', 302, 5)
    insert_books(conn, 'Муму', 'И. Тургенев', 1854, ' Рассказ', 90, 8)
    insert_books(conn, 'Белый пароход', 'Ч. Айтматов', 1970, 'Повесть', 418, 5)
    insert_books(conn, 'Материнское поле', 'Ч. Айтматов', 1963, 'Реализм', 326, 3)


