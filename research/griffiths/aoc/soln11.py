
def createMatrix(fileName):

    f = open(fileName)
    fileText = f.read()

    matrix = []

    for line in fileText.split('\n'):
        row = []
        for character in line:
            if character != '\n':
                row.append(int(character))
        matrix.append(row)

    return matrix

def inRange(matrix, x, y):
    if x < 0 or y < 0:
        return False

    if (x >= len(matrix)) or (y >= len(matrix[x])):
        return False

    return True

def incrementSurroundings(matrix, rowIndex, colIndex):
    for j in [-1, 0, 1]:
        for i in [-1, 0, 1]:
            newRowIndex = rowIndex + j
            newColIndex = colIndex + i
            if inRange(matrix, newRowIndex, newColIndex) and matrix[newRowIndex][newColIndex] != 0:
                matrix[newRowIndex][newColIndex] += 1

def startStep(matrix):
    for rowCounter in range(len(matrix)):
        for colCounter in range(len(matrix[rowCounter])):
            matrix[rowCounter][colCounter] = matrix[rowCounter][colCounter] + 1

    return doFlashes(matrix)

def doFlashes(matrix):
    # iterate over list and do flashes
    changeCounter = 0
    haveChangesOccured = False
    listToIncrement = []
    for rowCounter in range(len(matrix)):
        for colCounter in range(len(matrix[rowCounter])):
            if matrix[rowCounter][colCounter] > 9:
                listToIncrement.append((rowCounter, colCounter))
                matrix[rowCounter][colCounter] = 0
                changeCounter +=1 
                haveChangesOccured = True
    if haveChangesOccured:
        for (i, j) in listToIncrement:
            incrementSurroundings(matrix, i, j)
        return (changeCounter + doFlashes(matrix))
    else:
        return changeCounter

changeCounter = 0
matrix = createMatrix("input.txt")
for i in range(100):
    changeCounter += startStep(matrix)

print(changeCounter)

matrix = createMatrix("input.txt")
syncIter = 0
while(True):
    currentChangeNum = startStep(matrix)
    syncIter += 1
    if currentChangeNum == 100:
        break

print(syncIter)
