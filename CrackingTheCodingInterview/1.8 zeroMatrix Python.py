"""Write a program such that if an eleent in an MxN matrix is 0, its entire row and column are set to 0."""

"""Using the matrix itself as the memory is O(1) this program is however O(N^2) time, what it does though is
make two booleans for the first row and first column so that we that we know to clear those rows later if needed
so it goes through the matrix looking for 0s and if found puts it in the first row or column then later checking
the first row or column for 0s to clear that entire row."""

def zeroMatrix(matrix):
    firstRow = False
    firstCol = False

    for i in range(len(matrix)):
        if matrix[i][0] is 0:
            firstCol = True
            break;

    for j in range(len(matrix[0])):
        if matrix[0][j] is 0:
            firstRow = True
            break;

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] is 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(len(matrix)):
        if matrix[i][0] is 0:
            for m in range(len(matrix[0])):
                matrix[i][m] = 0

    for j in range(len(matrix[0])):
        if matrix[0][j] is 0:
            for n in range(len(matrix)):
                matrix[n][j] = 0

    if(firstRow):
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if(firstCol):
        for i in range(len(matrix)):
            matrix[i][0] = 0

    return matrix
