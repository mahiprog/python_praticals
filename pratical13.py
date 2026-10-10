import sqlite3


def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_record():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()

    print("Record added successfully.")


def display_records():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()

    if records:
        print("\nStudent Records:")
        for record in records:
            print(
                f"ID: {record[0]}, Name: {record[1]}, "
                f"Age: {record[2]}, Course: {record[3]}"
            )
    else:
        print("No records found.")

    conn.close()


def modify_record():
    student_id = int(input("Enter student ID to modify: "))

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE student SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Record modified successfully.")
    else:
        print("Record not found.")

    conn.close()


def delete_record():
    student_id = int(input("Enter student ID to delete: "))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Record deleted successfully.")
    else:
        print("Record not found.")

    conn.close()


def main():
    create_table()

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Modify Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_record()
            elif choice == "2":
                display_records()
            elif choice == "3":
                modify_record()
            elif choice == "4":
                delete_record()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()