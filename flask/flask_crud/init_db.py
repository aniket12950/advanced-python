import sqlite3
conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    join_date TEXT NOT NULL,
    salary REAL NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Employee database created successfully")
