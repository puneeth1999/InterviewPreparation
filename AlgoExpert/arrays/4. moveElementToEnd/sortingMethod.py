#Time complexity = O(nlogn) | Space complexity = O(1)
def moveElementToEnd(array, element):
    array.sort()
    for i in range(len(array)):
        if(array[i] is element):
            j = i+1
            i_ = i
            break
    while(array[j] == element and j<len(array)):
        j += 1
    secondArray = array[i:j]
    array = sorted(list(set(array) - set(secondArray)))
    for x in secondArray:
        array.append(x)
    return array

print(moveElementToEnd([2,1,2,2,2,3,4,2], 2))
