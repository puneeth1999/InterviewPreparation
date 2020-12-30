#Recursion
# Time complexity = O(n) since we only go through each element in the array only once.
# Space complexity = O(n) since we store all the element in the external array. If we just print the values
#instead of storing, then the space complexity becomes O(1).
'''
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
'''
def spiralTraverse(array):
    startRow = 0
    startColumn = 0
    endRow = len(array) - 1
    endColumn = len(array[0]) - 1
    result = []
    spiralFill(array, startRow, endRow, startColumn, endColumn, result)
    return result
def spiralFill(array, startRow, endRow, startColumn, endColumn, result):
    if startRow > endRow or startColumn > endColumn:
        return
    for col in range(startColumn, endColumn + 1):
        result.append(array[startRow][col])
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endColumn])
    for col in reversed(range(startColumn, endColumn)):
        result.append(array[endRow][col])
    for row in reversed(range(startRow + 1, endRow)):
        result.append(array[row][startRow])

    spiralFill(array, startRow + 1, endRow - 1, startColumn + 1, endColumn - 1, result)

print(spiralTraverse([[1,2,3,4], [12,13,14,5], [11,16,15,6],[10,9,8,7]]))
