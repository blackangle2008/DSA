def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    first_row = False
    first_col = False

    # Check first column
    for i in range(m):
        if matrix[i][0] == 0:
            first_col = True

    # Check first row
    for j in range(n):
        if matrix[0][j] == 0:
            first_row = True

    # Mark zeros in first row & column
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set matrix elements to zero based on marks
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Update first column
    if first_col:
        for i in range(m):
            matrix[i][0] = 0

    # Update first row
    if first_row:
        for j in range(n):
            matrix[0][j] = 0


# Example usage
matrix = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 1]
]

setZeroes(matrix)

# Print result
for row in matrix:
    print(*row)