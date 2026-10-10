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


def insert_record(name, age, course):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()


def search_record_by_id(student_id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE id = ?",
        (student_id,)
    )

    record = cursor.fetchone()
    conn.close()
    return record


def search_record_by_name(name):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE name LIKE ?",
        ("%" + name + "%",)
    )

    records = cursor.fetchall()
    conn.close()
    return records


def main():
    create_table()

    while True:
        print("\n1. Insert Record")
        print("2. Search by ID")
        print("3. Search by Name")
        print("4. Display Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")

            insert_record(name, age, course)
            print("Record inserted successfully.")

        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            record = search_record_by_id(student_id)

            if record:
                print("Student Record:", record)
            else:
                print("Record not found.")

        elif choice == "3":
            name = input("Enter student name: ")
            records = search_record_by_name(name)

            if records:
                for record in records:
                    print(record)
            else:
                print("Record not found.")

        elif choice == "4":
            conn = sqlite3.connect("students.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")

            for record in cursor.fetchall():
                print(record)

            conn.close()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()