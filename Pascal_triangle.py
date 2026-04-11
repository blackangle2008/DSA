def generate_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def print_triangle(triangle, n):
    for i in range(n):
        # Print spaces for alignment
        print(" " * (n - i - 1), end="")

        # Print row elements
        for num in triangle[i]:
            print(num, end=" ")
        print()


# Example usage
n = 10
triangle = generate_triangle(n)

print_triangle(triangle, n)