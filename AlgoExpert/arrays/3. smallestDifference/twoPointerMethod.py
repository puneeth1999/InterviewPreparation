#Time complexity = O(nlogn + mlogm) | Space complexity = O(1) //it's different for sorts though.
def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while (idxOne < len(array1) and idxTwo < len(array2)):
        firstNum = array1[idxOne]
        secondNum = array2[idxTwo]
        current = abs(firstNum - secondNum)
        if(firstNum < secondNum):
            idxOne += 1
        elif(firstNum > secondNum):
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if(current < smallest):
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
array1 = [-1,5,10,20,28,3]
array2 = [26,134,135,15,17]
print(smallestDifference(array1, array2))
