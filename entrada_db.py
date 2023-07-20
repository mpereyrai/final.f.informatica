import sqlite3

DATABASE_NAME = "entrada.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS entrada(
                id  PRIMARY KEY,
                estadio TEXT NOT NULL,
                partido TEXT NOT NULL,
                precio REAL NOT NULL,
                sector TEXT NOT NULL
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def insert_initial_data():
    data = [
        ("C001", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 10000, "Esquina"),
        ("C002", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 12000, "Plateas"),
        ("C003", "Buenos Aires Lawn Tennis Club", "Argentina-Lituania", 50000, "Palcos")
        
    ]
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='entrada'")
    table_exists = cursor.fetchone()

    if not table_exists:
       
        cursor.executemany("INSERT INTO entrada (id, estadio, partido, precio, sector) VALUES (?, ?, ?, ?, ?)", data)


    db.commit()



create_tables()
insert_initial_data()
