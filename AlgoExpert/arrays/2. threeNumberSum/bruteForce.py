#Time complexity = O(n^3) | Space complexity = O(1)
def threeNumberSum(array, targetSum):
    resultantTriplet = list()
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if(array[i] + array[j] + array[k] == targetSum):
                    resultantTriplet.append([array[i], array[j], array[k]])
    return resultantTriplet

array = [-8,-6,1,2,3,5,6,12]
targetSum = 0
print(threeNumberSum(array, targetSum))
