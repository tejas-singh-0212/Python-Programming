row_1 = int(input("Enter the number of rows for the first matrix: "))
col_1 = int(input("Enter the number of columns for the first matrix: "))
row_2 = int(input("Enter the number of rows for the second matrix: "))
col_2 = int(input("Enter the number of columns for the second matrix: "))
if col_1 != row_2:
    print("Error: The number of columns in the first matrix must equal the number of rows in the second matrix.")
else:
    print("\nEnter the elements of the first matrix:")
    a = []
    for i in range(row_1):
        row = []
        for j in range(col_1):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        a.append(row)
    print("\nEnter the elements of the second matrix:")
    b = []
    for i in range(row_2):
        row = []
        for j in range(col_2):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(element)
        b.append(row)
    pro = []
    for i in range(row_1):
        row = []
        for j in range(col_2):
            row.append(0)
        pro.append(row)
    for i in range(row_1):
        for j in range(col_2):
            pro[i][j] = 0
            for k in range(col_1):
                pro[i][j] += a[i][k] * b[k][j]
    print("\nProduct of the two matrices:")
    for i in range(row_1):
        for j in range(col_2):
            print(pro[i][j], end="\t")
        print()