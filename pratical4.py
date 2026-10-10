def fibonacci_series(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def main():
    try:
        n = int(input("Enter the number of terms in the Fibonacci series: "))

        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            print("Fibonacci series:", fibonacci_series(n))

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()