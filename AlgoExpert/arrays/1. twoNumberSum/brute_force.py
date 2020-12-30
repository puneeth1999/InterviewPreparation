#Time Complexity O(n^2) | Space Complexity O(1)
def find_number_sum(arr, sum_needed):
    flag = 0
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if(arr[i] + arr[j] == sum_needed):
                print('The required pair is:', arr[i], 'and', arr[j])
                flag = 1
                break
    if flag is 0:
        print('Could not find a two sum pair')

arr = [1,2,-3,-4,5,6]
find_number_sum(arr, 7)
