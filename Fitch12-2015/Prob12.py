def main():
    for i in range(1):
        matrix = [[0] * 9 for j in range(9)]
        for j in range(9):
            matrix[j] = list(input())
        for row in range(9):
            for col in range(9):
                matrix[row][col] = int(matrix[row][col])
        if isBroken(matrix):
            print("already broken")
        else:
            print(solve(matrix))

def solve(matrix):
    total = 0
    if isBroken(matrix):
        # print("This is broken")
        return -1
    elif isFinished(matrix):
        print("Matrix is finished.")
        return 1
    else:
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == 0:
                    for i in range(9):
                        matrix[row][col] = i + 1
                        # print("Assigned: " + str(matrix[row][col]) + " to row " + str(row) + " col " + str(col))
                        if solve(matrix) != -1:
                            total += 1
                            print("Increment total")
                            return total
                        else:
                            if matrix[row][col] == 9:
                                matrix[row][col] = 0
                                print("Ran out of options")
                                print("Row: " + str(row) + " Col: " + str(col))
                                if row == 8 and col == 8:
                                    for row in matrix:
                                        print(row)
                                return -1
                            matrix[row][col] = 0
        if total != 0:
            return total
        else:
            print("Could not solve")
            return -1

def isFinished(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return False
    return True

def isBroken(matrix):
    for i in range(9):
        temp = [0 for i in range(9)]
        for j in range(9):
            cell = matrix[i][j]
            if int(cell) != 0:
                temp[int(cell) - 1] += 1
                if temp[int(cell) - 1] > 1:
                    return True
    for i in range(9):
        temp = [0 for i in range(9)]
        for j in range(9):
            cell = int(matrix[j][i])
            if int(cell) != 0:
                temp[cell - 1] += 1
                if temp[cell - 1] > 1:
                    return True
    rowBase = 0
    colBase = 0
    for i in range(9):
        temp = [0 for i in range(9)]
        for j in range(3):
            rowCoord = rowBase + j
            for k in range(3):
                colCoord = colBase + k
                cell = int(matrix[rowCoord][colCoord])
                if cell != 0:
                    temp[cell - 1] += 1
                    if temp[cell - 1] > 1:
                        return True
        if (i + 1) % 3 == 0:
            rowBase += 3
        if colBase != 6:
            colBase += 3
        else:
            colBase = 0
    return False

if __name__ == "__main__": main()

# 674138952
# 159247638
# 328569714
# 542396871
# 791825346
# 863014529
# 236971485
# 987452163
# 415783297

# 004038900
# 109040000
# 020000710
# 000306001
# 790000046
# 800704000
# 036000080
# 000050103
# 005680200
