from database import create_database

from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from marks import (
    add_marks,
    view_marks
)

from attendance import (
    add_attendance,
    view_attendance
)


def menu():
    while True:
        print("\n" + "=" * 50)
        print("        STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. View Marks")
        print("8. Add Attendance")
        print("9. View Attendance")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            view_marks()

        elif choice == "8":
            add_attendance()

        elif choice == "9":
            view_attendance()

        elif choice == "10":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


def main():
    create_database()
    menu()


if __name__ == "__main__":
    main()