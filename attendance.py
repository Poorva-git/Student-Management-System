import sqlite3

DATABASE = "students.db"


def add_attendance():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number: "))
    except ValueError:
        print("Invalid Roll Number!")
        conn.close()
        return

    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found!")
        conn.close()
        return

    try:
        total_classes = int(input("Enter Total Classes: "))
        present = int(input("Enter Classes Attended: "))
    except ValueError:
        print("Please enter valid numbers.")
        conn.close()
        return

    if total_classes <= 0:
        print("Total classes must be greater than 0.")
        conn.close()
        return

    if present > total_classes:
        print("Present classes cannot exceed total classes.")
        conn.close()
        return

    attendance_percent = (present / total_classes) * 100

    cursor.execute("SELECT * FROM attendance WHERE roll_no=?", (roll,))

    if cursor.fetchone():
        cursor.execute("""
            UPDATE attendance
            SET total_classes=?,
                present=?,
                attendance_percent=?
            WHERE roll_no=?
        """, (
            total_classes,
            present,
            attendance_percent,
            roll
        ))
    else:
        cursor.execute("""
            INSERT INTO attendance
            VALUES (?,?,?,?)
        """, (
            roll,
            total_classes,
            present,
            attendance_percent
        ))

    conn.commit()
    conn.close()

    print("\nAttendance Saved Successfully!")


def view_attendance():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.roll_no,
          students.name,
          attendance.total_classes,
          attendance.present,
          attendance.attendance_percent
        FROM students
        JOIN attendance
        ON students.roll_no = attendance.roll_no
    """)

    rows = cursor.fetchall()

    if not rows:
        print("\nNo attendance records found.")
        conn.close()
        return

    print("\n" + "=" * 80)
    print(f"{'Roll':<8}{'Name':<20}{'Total':<10}{'Present':<10}{'Attendance %'}")
    print("=" * 80)

    for row in rows:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<10}{row[3]:<10}{row[4]:.2f}")

    print("=" * 80)

    conn.close()