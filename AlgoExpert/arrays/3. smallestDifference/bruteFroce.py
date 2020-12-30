#Time complexity = O(n*m) | Space complexity = O(1)
def smallestDifference(array1, array2):
    resultArray = []
    smallDiff = max(array1[0], array2[0]) - min(array1[0], array2[0])
    for i in range(len(array1)):
        for j in range(len(array2)):
            diff = max(array1[i], array2[j]) - min(array1[i], array2[j])
            if(diff < smallDiff):
                resultArray.clear()
                resultArray.append((array1[i], array2[j]))
                smallDiff = diff
            else:
                continue
    return resultArray
array1 = [-1,5,10,20,28,3]
array2 = [26,134,135,15,17]
print(smallestDifference(array1, array2))
