#Very much prone to error. Especially if arra[0] and array[1] are equal.
#Time complexity = O(n) | Space complexity = O(1)
def monotonicArray(array):
    if array[1] > array[0]:
        init_direction = 'up'
    elif array[1] < array[0]:
        init_direction = 'down'
    else:
        init_direction = 'flat'
    for i in range(2, len(array) - 1):
        j = i + 1
        if array[j] > array[i]:
            direction = 'up'
        elif array[j] < array[i]:
            direction = 'down'
        else:
            direction = 'flat'
        if (direction == init_direction):
            pass
        elif(direction == 'flat'):
            pass
        else:
            return False
    return True
print(monotonicArray([-1,-5,-10,-1100,-1100, -1101,-1102,-9001]))
