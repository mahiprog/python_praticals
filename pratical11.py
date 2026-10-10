import sqlite3


def create_table():
    with sqlite3.connect("students.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL
            )
        """)


def insert_record(name, age, course):
    with sqlite3.connect("students.db") as conn:
        conn.execute(
            "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )


def display_records():
    with sqlite3.connect("students.db") as conn:
        records = conn.execute(
            "SELECT * FROM student"
        ).fetchall()

    if records:
        print("\nStudent Records:")
        for row in records:
            print(
                f"ID: {row[0]}, Name: {row[1]}, "
                f"Age: {row[2]}, Course: {row[3]}"
            )
    else:
        print("No records found.")


def search_record_by_id(student_id):
    with sqlite3.connect("students.db") as conn:
        return conn.execute(
            "SELECT * FROM student WHERE id = ?",
            (student_id,)
        ).fetchone()


def search_record_by_name(name):
    with sqlite3.connect("students.db") as conn:
        return conn.execute(
            "SELECT * FROM student WHERE name LIKE ?",
            (f"%{name}%",)
        ).fetchall()


def main():
    create_table()

    while True:
        print("\n1. Insert Record")
        print("2. Display Records")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter name: ").strip()
                age = int(input("Enter age: "))
                course = input("Enter course: ").strip()

                if not name or not course or age < 0:
                    print("Enter valid student details.")
                    continue

                insert_record(name, age, course)
                print("Record inserted successfully.")

            elif choice == "2":
                display_records()

            elif choice == "3":
                student_id = int(input("Enter student ID: "))
                record = search_record_by_id(student_id)
                print(record if record else "Record not found.")

            elif choice == "4":
                name = input("Enter student name: ")
                records = search_record_by_name(name)

                for record in records:
                    print(record)

                if not records:
                    print("No matching records found.")

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()