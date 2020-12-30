#Time Complexity: O(n) | Space Complexity: O(n) (because we keep adding elements to the hash table)
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        differnce = targetSum - num
        if(differnce in nums):
            return [num, differnce]
        else:
            nums[num] = True
    return 'No match found'

array = [-1,5,6,7,8,9,11]
print(twoNumberSum(array, 10))
