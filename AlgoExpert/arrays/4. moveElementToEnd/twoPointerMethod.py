#Time complexity = O(n) | Space complexity = O(1)
def moveElementToEnd(array, targetElement):
    i = 0
    j = len(array) - 1
    while (i < j):
        if array[j] is targetElement:
            j -= 1
        elif array[i] is targetElement:
            array[i], array[j] = array[j], array[i] #Swapping
        else:
            i += 1
    return array
print(moveElementToEnd([2,1,2,2,2,3,4,2], 2))
