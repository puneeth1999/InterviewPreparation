'''
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
'''
def rotateImage(a):
    #STEP - 1: TRANSPOSE THE ARRAY (Swap a[i][j] and a[j][i])
    for i in range(len(a)):
        for j in range(i, len(a)):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp

    #STEP - 2: Switch the columns (Swap a[i][j] and a[i][N-1-j])
    for i in range(len(a)):
        for j in range(len(a)//2):
            temp = a[i][j]
            a[i][j] = a[i][len(a)-1-j]
            a[i][len(a)-1-j] = temp
    return a
