def input_matrix(rows, cols, name):
    matrix = []

    for i in range(rows):
        while True:
            raw = input(
                f"Enter row {i + 1} of Matrix {name} ({cols} integers separated by spaces): "
            ).strip()

            if not raw:
                print("Please enter integers only.")
                continue

            try:
                row = list(map(int, raw.replace(",", " ").split()))

                if len(row) == cols:
                    matrix.append(row)
                    break

                print(f"Enter exactly {cols} integers separated by spaces.")

            except ValueError:
                print("Please enter integers only.")

    return matrix


def add_matrices(A, B):
    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def multiply_matrices(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def main():
    try:
        r1 = int(input("Rows for Matrix A: "))
        c1 = int(input("Columns for Matrix A: "))
        r2 = int(input("Rows for Matrix B: "))
        c2 = int(input("Columns for Matrix B: "))

        if min(r1, c1, r2, c2) <= 0:
            print("Dimensions must be positive.")
            return

        A = input_matrix(r1, c1, "A")
        B = input_matrix(r2, c2, "B")

        if r1 == r2 and c1 == c2:
            print("Matrix Addition:")
            for row in add_matrices(A, B):
                print(row)
        else:
            print("Matrix addition is not possible.")

        if c1 == r2:
            print("Matrix Multiplication:")
            for row in multiply_matrices(A, B):
                print(row)
        else:
            print("Matrix multiplication is not possible.")

    except ValueError:
        print("Invalid input. Enter integers only.")


if __name__ == "__main__":
    main()