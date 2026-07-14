import sqlite3
import csv
from openpyxl import Workbook

DATABASE = "students.db"


def export_csv():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.roll_no,
              s.name,
              s.course,
              m.python,
              m.dbms,
              m.dsa,
              m.ai,
              m.total,
              m.percentage,
              m.gpa,
              a.total_classes,
              a.present,
              a.attendance_percent
        FROM students s
        LEFT JOIN marks m
        ON s.roll_no=m.roll_no
        LEFT JOIN attendance a
        ON s.roll_no=a.roll_no
    """)

    data = cursor.fetchall()

    with open("students_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Roll No",
            "Name",
            "Course",
            "Python",
            "DBMS",
            "DSA",
            "AI",
            "Total",
            "Percentage",
            "GPA",
            "Total Classes",
            "Present",
            "Attendance %"
        ])

        writer.writerows(data)

    conn.close()

    print("\n✅ CSV Exported Successfully!")
    print("File Name : students_report.csv")


def export_excel():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.roll_no,
          s.name,
        s.course,
            m.python,
            m.dbms,
            m.dsa,
              m.ai,
              m.total,
              m.percentage,
              m.gpa,
              a.total_classes,
              a.present,
              a.attendance_percent
        FROM students s
        LEFT JOIN marks m
        ON s.roll_no=m.roll_no
        LEFT JOIN attendance a
        ON s.roll_no=a.roll_no
    """)

    data = cursor.fetchall()

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Student Report"

    headers = [
        "Roll No",
        "Name",
        "Course",
        "Python",
        "DBMS",
        "DSA",
        "AI",
        "Total",
        "Percentage",
        "GPA",
        "Total Classes",
        "Present",
        "Attendance %"
    ]

    sheet.append(headers)

    for row in data:
        sheet.append(row)

    workbook.save("students_report.xlsx")

    conn.close()

    print("\n✅ Excel Exported Successfully!")
    print("File Name : students_report.xlsx")