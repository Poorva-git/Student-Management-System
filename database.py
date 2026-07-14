import sqlite3

DATABASE = "students.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # ---------------- Students ---------------- #

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll_no INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL,
        phone TEXT,
        email TEXT
    )
    """)

    # ---------------- Marks ---------------- #

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marks(
        roll_no INTEGER PRIMARY KEY,
        python INTEGER DEFAULT 0,
        dbms INTEGER DEFAULT 0,
        dsa INTEGER DEFAULT 0,
        ai INTEGER DEFAULT 0,
        total INTEGER DEFAULT 0,
        percentage REAL DEFAULT 0,
        gpa REAL DEFAULT 0,
        FOREIGN KEY(roll_no) REFERENCES students(roll_no)
    )
    """)

    # ---------------- Attendance ---------------- #

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        roll_no INTEGER PRIMARY KEY,
        total_classes INTEGER DEFAULT 0,
        present INTEGER DEFAULT 0,
        attendance_percent REAL DEFAULT 0,
        FOREIGN KEY(roll_no) REFERENCES students(roll_no)
    )
    """)

    # ---------------- Users ---------------- #

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Default Admin

    cursor.execute("""
    INSERT OR IGNORE INTO users(username,password,role)
    VALUES('admin','admin123','Admin')
    """)

    conn.commit()
    conn.close()