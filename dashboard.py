import sqlite3

DATABASE = "students.db"


def show_dashboard():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Highest GPA
    cursor.execute("SELECT MAX(gpa) FROM marks")
    highest_gpa = cursor.fetchone()[0]

    if highest_gpa is None:
        highest_gpa = 0

    # Average Attendance
    cursor.execute("SELECT AVG(attendance_percent) FROM attendance")
    avg_attendance = cursor.fetchone()[0]

    if avg_attendance is None:
        avg_attendance = 0

    # Students Passed
    cursor.execute("SELECT COUNT(*) FROM marks WHERE percentage >= 40")
    passed = cursor.fetchone()[0]

    # Students Failed
    cursor.execute("SELECT COUNT(*) FROM marks WHERE percentage < 40")
    failed = cursor.fetchone()[0]

    conn.close()

    print("\n" + "=" * 55)
    print("               DASHBOARD")
    print("=" * 55)

    print(f"Total Students      : {total_students}")
    print(f"Highest GPA         : {highest_gpa}")
    print(f"Average Attendance  : {avg_attendance:.2f}%")
    print(f"Students Passed     : {passed}")
    print(f"Students Failed     : {failed}")

    print("=" * 55)