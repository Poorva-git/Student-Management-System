import sqlite3

DATABASE = "students.db"


def student_report():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number: "))
    except ValueError:
        print("Invalid Roll Number!")
        conn.close()
        return

    cursor.execute("""
        SELECT s.roll_no,
          s.name,
        s.course,
        m.python,
        m.dbms,m.dsa,
          m.ai,
          m.total,
          m.percentage,
          m.gpa,
          a.attendance_percent
        FROM students s
        LEFT JOIN marks m
            ON s.roll_no = m.roll_no
        LEFT JOIN attendance a
            ON s.roll_no = a.roll_no
        WHERE s.roll_no = ?
    """, (roll,))

    student = cursor.fetchone()

    if student is None:
        print("\nStudent Not Found!")
        conn.close()
        return

    attendance = student[10] if student[10] is not None else 0
    percentage = student[8] if student[8] is not None else 0
    gpa = student[9] if student[9] is not None else 0

    result = "PASS" if percentage >= 40 else "FAIL"

    print("\n" + "=" * 60)
    print("              STUDENT REPORT CARD")
    print("=" * 60)

    print(f"Roll Number : {student[0]}")
    print(f"Name        : {student[1]}")
    print(f"Course      : {student[2]}")

    print("\n----------- Marks -----------")

    print(f"Python      : {student[3] if student[3] is not None else 0}")
    print(f"DBMS        : {student[4] if student[4] is not None else 0}")
    print(f"DSA         : {student[5] if student[5] is not None else 0}")
    print(f"AI          : {student[6] if student[6] is not None else 0}")

    print("-----------------------------")
    print(f"Total       : {student[7] if student[7] is not None else 0}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"GPA         : {gpa}")
    print(f"Attendance  : {attendance:.2f}%")
    print(f"Result      : {result}")

    print("=" * 60)

    conn.close()


def topper():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.roll_no,
            
            students.name,
            marks.percentage,
            marks.gpa
        FROM students
        JOIN marks
        ON students.roll_no = marks.roll_no
        ORDER BY marks.percentage DESC
        LIMIT 1
    """)

    student = cursor.fetchone()

    if student is None:
        print("\nNo Records Found!")
        conn.close()
        return

    print("\n" + "=" * 50)
    print("               TOPPER")
    print("=" * 50)

    print(f"Roll Number : {student[0]}")
    print(f"Name        : {student[1]}")
    print(f"Percentage  : {student[2]:.2f}%")
    print(f"GPA         : {student[3]}")

    print("=" * 50)

    conn.close()


def rank_list():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.roll_no,
          students.name,
            marks.percentage,
            marks.gpa
        FROM students
        JOIN marks
        ON students.roll_no = marks.roll_no
        ORDER BY marks.percentage DESC
    """)

    data = cursor.fetchall()

    if not data:
        print("\nNo Records Found!")
        conn.close()
        return

    print("\n" + "=" * 70)
    print(f"{'Rank':<8}{'Roll':<10}{'Name':<20}{'Percentage':<15}{'GPA'}")
    print("=" * 70)

    rank = 1

    for student in data:
        print(
            f"{rank:<8}"
            f"{student[0]:<10}"
            f"{student[1]:<20}"
            f"{student[2]:<15.2f}"
            f"{student[3]}"
        )
        rank += 1

    print("=" * 70)

    conn.close()