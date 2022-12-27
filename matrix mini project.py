def forEvenNumber(n):
    a = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            a[i][j] = (n * n + 1) - a[i][j];
    for i in range(0, n // 4):
        for j in range(3 * (n // 4), n):
            a[i][j] = (n * n + 1) - a[i][j];
    for i in range(3 * (n // 4), n):
        for j in range(0, n // 4):
            a[i][j] = (n * n + 1) - a[i][j];
    for i in range(3 * (n // 4), n):
        for j in range(3 * (n // 4), n):
            a[i][j] = (n * n + 1) - a[i][j];
    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            a[i][j] = (n * n + 1) - a[i][j];
    print("\nSum from all sides of  the matrix is = ",
          n * (n * n + 1) // 2, "\n")
    for i in range(n):
        for j in range(n):
            print('%2d ' % (a[i][j]), end=" ")
        print()
def forOddNumber(n):
    mgsqr = [[0 for x in range(n)]
             for y in range(n)]
    r = n // 2
    c = n - 1
    num = 1
    while num <= (n * n):
        if r == -1 and c == n:
            c = n - 2
            r = 0
        else:
            if c == n:
                c = 0
            if r < 0:
                r = n - 1
        if mgsqr[int(r)][int(c)]:
            c = c - 2
            r = r + 1
            continue
        else:
            mgsqr[int(r)][int(c)] = num
            num = num + 1
        c = c + 1
        r = r - 1
    print("\nSum of all row, column and diagonals= ",
          n * (n * n + 1) // 2, "\n")
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (mgsqr[i][j]), end='')
        print()
n = int(input("Please Enter Number of Rows and Column (n*n): "))
if n%2==0:
    forEvenNumber(n)
else:
    forOddNumber(n)
