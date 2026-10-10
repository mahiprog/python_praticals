def read_last_five_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("Last five lines of the file:")

        for line in lines[-5:]:
            print(line, end="")

    except FileNotFoundError:
        print("Error: File not found.")

    except OSError as error:
        print("Error reading file:", error)


def main():
    filename = input("Enter the filename: ")
    read_last_five_lines(filename)


if __name__ == "__main__":
    main()