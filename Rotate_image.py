# Function to rotate matrix 90 degree clockwise
def rotateImage(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


# Function to print matrix
def printMatrix(matrix):
    for row in matrix:
        print(*row)


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
printMatrix(matrix)

rotateImage(matrix)

print("\nRotated Matrix (90° Clockwise):")
printMatrix(matrix)