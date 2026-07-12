import sqlite3

DATABASE = "students.db"


def calculate_gpa(percentage):
    if percentage >= 90:
        return 10
    elif percentage >= 80:
        return 9
    elif percentage >= 70:
        return 8
    elif percentage >= 60:
        return 7
    elif percentage >= 50:
        return 6
    else:
        return 5


# ---------------- ADD / UPDATE MARKS ---------------- #

def add_marks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number: "))
    except ValueError:
        print("Invalid Roll Number.")
        conn.close()
        return

    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    if cursor.fetchone() is None:
        print("Student not found.")
        conn.close()
        return

    try:
        python_marks = int(input("Python: "))
        dbms = int(input("DBMS: "))
        dsa = int(input("DSA: "))
        ai = int(input("AI: "))
    except ValueError:
        print("Marks must be integers.")
        conn.close()
        return

    marks = [python_marks, dbms, dsa, ai]

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Marks should be between 0 and 100.")
        conn.close()
        return

    total = sum(marks)
    percentage = total / 4
    gpa = calculate_gpa(percentage)

    cursor.execute("SELECT * FROM marks WHERE roll_no = ?", (roll,))

    if cursor.fetchone():
        cursor.execute("""
            UPDATE marks
            SET python=?,
                dbms=?,
                dsa=?,
                ai=?,
                total=?,
                percentage=?,
                gpa=?
            WHERE roll_no=?
        """, (
            python_marks,
            dbms,
            dsa,
            ai,
            total,
            percentage,
            gpa,
            roll
        ))
    else:
        cursor.execute("""
            INSERT INTO marks
            VALUES (?,?,?,?,?,?,?,?)
        """, (
            roll,
            python_marks,
            dbms,
            dsa,
            ai,
            total,
            percentage,
            gpa
        ))

    conn.commit()
    conn.close()

    print("\nMarks Added Successfully!")


# ---------------- VIEW MARKS ---------------- #

def view_marks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.roll_no,
               students.name,
               marks.python,
               marks.dbms,
               marks.dsa,
               marks.ai,
               marks.total,
               marks.percentage,
               marks.gpa
        FROM students
        JOIN marks
        ON students.roll_no = marks.roll_no
    """)

    data = cursor.fetchall()

    if not data:
        print("\nNo marks found.")
        conn.close()
        return

    print("\n" + "=" * 110)
    print(f"{'Roll':<8}{'Name':<18}{'Python':<10}{'DBMS':<8}{'DSA':<8}{'AI':<8}{'Total':<8}{'Percentage':<12}{'GPA'}")
    print("=" * 110)

    for row in data:
        print(f"{row[0]:<8}{row[1]:<18}{row[2]:<10}{row[3]:<8}{row[4]:<8}{row[5]:<8}{row[6]:<8}{row[7]:<12.2f}{row[8]}")

    print("=" * 110)

    conn.close()