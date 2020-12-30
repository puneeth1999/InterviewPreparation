#Time Complexity: O(N) | Space Complexity: O(1)
a = [-10, -5, 1, 3, 6, 9]
output = [0 for i in range(len(a))]
i = 0
j = len(a) - 1
k = j
while k>=0:
    if abs(a[i]) < abs(a[j]):
        output[k] = a[j]**2
        j -= 1
    else:
        output[k] = a[i]**2
        i+=1
    k-=1
print(output)
