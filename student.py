import sqlite3

DATABASE = "students.db"


# ---------------- ADD STUDENT ---------------- #

def add_student():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("\n===== Add Student =====")

    try:
        roll = int(input("Enter Roll Number: "))
    except ValueError:
        print("Roll number must be an integer.")
        conn.close()
        return

    # Check duplicate roll number
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    if cursor.fetchone():
        print("A student with this roll number already exists.")
        conn.close()
        return

    name = input("Enter Name: ").strip()

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Age must be an integer.")
        conn.close()
        return

    course = input("Enter Course: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    # Validation
    if len(phone) != 10 or not phone.isdigit():
        print("Phone number must contain exactly 10 digits.")
        conn.close()
        return

    if "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO students
        (roll_no, name, age, course, phone, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (roll, name, age, course, phone, email))

    conn.commit()
    conn.close()

    print("\nStudent added successfully!")


# ---------------- VIEW STUDENTS ---------------- #

def view_students():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("\nNo student records found.")
        conn.close()
        return

    print("\n" + "=" * 90)
    print(f"{'Roll':<8}{'Name':<20}{'Age':<8}{'Course':<18}{'Phone':<15}{'Email'}")
    print("=" * 90)

    for student in students:
        print(f"{student[0]:<8}{student[1]:<20}{student[2]:<8}{student[3]:<18}{student[4]:<15}{student[5]}")

    print("=" * 90)

    conn.close()


# ---------------- SEARCH STUDENT ---------------- #

def search_student():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number: "))
    except ValueError:
        print("Invalid Roll Number.")
        conn.close()
        return

    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("-" * 35)
        print(f"Roll Number : {student[0]}")
        print(f"Name        : {student[1]}")
        print(f"Age         : {student[2]}")
        print(f"Course      : {student[3]}")
        print(f"Phone       : {student[4]}")
        print(f"Email       : {student[5]}")
    else:
        print("\nStudent not found.")

    conn.close()


# ---------------- UPDATE STUDENT ---------------- #

def update_student():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number to Update: "))
    except ValueError:
        print("Invalid Roll Number.")
        conn.close()
        return

    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    print("\nLeave blank if you don't want to change a field.")

    name = input(f"Name ({student[1]}): ").strip()
    age = input(f"Age ({student[2]}): ").strip()
    course = input(f"Course ({student[3]}): ").strip()
    phone = input(f"Phone ({student[4]}): ").strip()
    email = input(f"Email ({student[5]}): ").strip()

    updated_name = name if name else student[1]
    updated_age = int(age) if age else student[2]
    updated_course = course if course else student[3]
    updated_phone = phone if phone else student[4]
    updated_email = email if email else student[5]

    cursor.execute("""
        UPDATE students
        SET name = ?,
            age = ?,
            course = ?,
            phone = ?,
            email = ?
        WHERE roll_no = ?
    """, (
        updated_name,
        updated_age,
        updated_course,
        updated_phone,
        updated_email,
        roll
    ))

    conn.commit()
    conn.close()

    print("\nStudent Updated Successfully!")


# ---------------- DELETE STUDENT ---------------- #

def delete_student():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        roll = int(input("\nEnter Roll Number to Delete: "))
    except ValueError:
        print("Invalid Roll Number.")
        conn.close()
        return

    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        return

    confirm = input(f"Delete {student[1]}? (y/n): ")

    if confirm.lower() == "y":
        cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll,))
        conn.commit()
        print("Student Deleted Successfully!")
    else:
        print("Deletion Cancelled.")

    conn.close()