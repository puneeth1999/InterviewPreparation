#Time complexity = O(n) Since each element is only visited once.
#Space complexity = O(1) Since we need to keep adding peaks to another array.
def longestPeak(array):
    longestPeak = 0
    i = 1

    while i < (len(array) - 1):
        isPeak = array[i - 1] < array[i] and array[i + 1] < array[i]

        if not isPeak:
            i += 1
            continue
        leftidx = i - 2
        rightidx = i + 2

        while leftidx >= 0 and array[leftidx] < array[leftidx + 1]:
            leftidx -= 1
        while rightidx <= len(array) - 1 and array[rightidx] < array[rightidx - 1]:
            rightidx += 1
        lengthOfThePeak = rightidx - leftidx - 1
        if lengthOfThePeak > longestPeak:
            longestPeak = lengthOfThePeak

        i += 1
    return longestPeak

array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(array))
