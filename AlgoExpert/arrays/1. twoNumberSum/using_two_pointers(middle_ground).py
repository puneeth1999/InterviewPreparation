#Time complexity: O(nlogn) | Space complexity: O(1)
def twoNumberSum(array, targetSum):
    array.sort() #Use good algos like MergeSort or HeapSort or QuickSort which makes the complexity O(nlogn) already.
    left = 0
    right = len(array) -  1
    while left != right: #Covers the loop once in the worst case anf hence the time complexity of this loop is O(n)
        sum = array[left] + array[right]
        if sum is targetSum:
            return [array[left], array[right]]
        else:
            if sum < targetSum:
                left += 1
            elif sum > targetSum:
                right -= 1
    return []

array = [-1,5,-6,7,8,9,11]
print(twoNumberSum(array, 10))
