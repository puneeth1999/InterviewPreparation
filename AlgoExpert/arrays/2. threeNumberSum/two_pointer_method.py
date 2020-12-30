#Time complexity = O(n^2) | Space complexity = O(n)s
def threeNumberSum(array, targetSum):
    resultArray = list()
    for i in range(len(array) - 2):
        left = i+1
        right = len(array)-1
        while (left < right):
            currentSum = array[left] + array[right] + array[i]
            if(currentSum == targetSum):
                resultArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif(currentSum < targetSum):
                left += 1
            elif(currentSum > targetSum):
                right -= 1
    return resultArray

array = [-8,-6,1,2,3,5,6,12]
targetSum = 0
print(threeNumberSum(array, targetSum))
