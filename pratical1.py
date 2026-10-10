def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32


def main():
    while True:
        print("\nTemperature Conversion Menu")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{f:.2f}°F = {c:.2f}°C")

        elif choice == "2":
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{c:.2f}°C = {f:.2f}°F")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()