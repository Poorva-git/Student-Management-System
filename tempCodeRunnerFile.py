from database import create_database
from auth import login

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

from reports import (
    student_report,
    topper,
    rank_list
)

from dashboard import (
    show_dashboard
)

from export import (
    export_csv,
    export_excel
)


def menu():

    while True:

        print("\n" + "=" * 60)
        print("         STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")

        print("\n------ Marks ------")
        print("6. Add Marks")
        print("7. View Marks")

        print("\n------ Attendance ------")
        print("8. Add Attendance")
        print("9. View Attendance")

        print("\n------ Reports ------")
        print("10. Student Report Card")
        print("11. Topper")
        print("12. Rank List")

        print("\n------ Dashboard ------")
        print("13. Dashboard Statistics")

        print("\n------ Export ------")
        print("14. Export CSV")
        print("15. Export Excel")

        print("\n16. Logout")
        print("17. Exit")

        choice = input("\nEnter Choice : ")

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
            student_report()

        elif choice == "11":
            topper()

        elif choice == "12":
            rank_list()

        elif choice == "13":
            show_dashboard()

        elif choice == "14":
            export_csv()

        elif choice == "15":
            export_excel()

        elif choice == "16":
            print("\nLogged Out Successfully!\n")
            return

        elif choice == "17":
            print("\nThank You For Using Student Management System!")
            exit()

        else:
            print("\nInvalid Choice!")


def main():

    create_database()

    while True:

        print("\n" + "=" * 60)
        print("           STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)

        if login():
            menu()
        else:
            print("\nGood Bye!")
            break


if __name__ == "__main__":
    main()