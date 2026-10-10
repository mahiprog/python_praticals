def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except TypeError:
        print("Error: Please enter numeric values.")

    finally:
        print("Execution of divide_numbers() is complete.")


def main():
    try:
        x = float(input("Enter the numerator: "))
        y = float(input("Enter the denominator: "))
        divide_numbers(x, y)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()