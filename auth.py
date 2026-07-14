import sqlite3
import getpass

DATABASE = "students.db"


def admin_login():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("\n========== ADMIN LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")
    cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=? AND role='Admin'
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:
        print("\n✅ Login Successful!\n")
        return True
    else:
        print("\n❌ Invalid Username or Password!\n")
        return False


def student_login():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("\n========== STUDENT LOGIN ==========")

    try:
        roll = int(input("Roll Number: "))
    except ValueError:
        print("Invalid Roll Number.")
        conn.close()
        return False

    phone = input("Phone Number: ")

    cursor.execute("""
        SELECT * FROM students
        WHERE roll_no=? AND phone=?
    """, (roll, phone))

    student = cursor.fetchone()

    conn.close()

    if student:
        print(f"\n✅ Welcome {student[1]}!\n")
        return True
    else:
        print("\n❌ Invalid Roll Number or Phone Number!\n")
        return False


def login():
    while True:
        print("\n========== LOGIN ==========")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            return admin_login()

        elif choice == "2":
            return student_login()

        elif choice == "3":
            return False

        else:
            print("Invalid Choice!")