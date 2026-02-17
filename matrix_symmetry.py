rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
if rows != cols:
    print("Matrix must be square to be symmetric")
else:
    print(f"\nEnter {rows}x{cols} matrix elements:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)
    print("\nInput Matrix is:")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end="\t")
        print()
    
    is_symmetric = True
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
                break
        if not is_symmetric:
            break
    if is_symmetric:
        print("The matrix is SYMMETRIC!")
    else:
        print("The matrix is NOT SYMMETRIC!")