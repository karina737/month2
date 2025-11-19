import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT        
    )
                 
     """)
    
def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?,?,?)
                 """, 
    (name, age, city))
    conn.commit()

if __name__=='__main__':
    conn = sqlite3.connect('database.db')
    create_table(conn)
    add_student(conn, 'Igor', 30, 'Bishkek')
    add_student(conn, 'Karina', 27, 'Bishkek')

