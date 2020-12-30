#Time complexity = O(n) Since each element is only visited once.
#Space complexity = O(n) Since we need to keep adding peaks to another array.
def longestPeak(array):
    peak_indices = []
    finalCount = 0

    for i in range(1,len(array) - 1):
        before = array[i - 1]
        after = array[i + 1]
        if(before < array[i] and after < array[i]):
            peak_indices.append(i)
    for index in peak_indices:
        counter = 1 #Since the peak itself is to be calculated.
        i = index - 1
        j = index + 1
        peak = array[index]
        while i >= 0 and array[i] < array[i+1]:
            counter += 1
            i -= 1
        while j <= len(array) - 1 and array[j] < array[j-1]:
            counter += 1
            j += 1
        if counter > finalCount:
            finalCount = counter
    return finalCount
array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(array))
#We can actually do this without parting the problem. Check out the other .py file within the directory
