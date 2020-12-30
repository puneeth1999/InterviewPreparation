#Time complexity = O(n) | Space complexity = O(1)
def monotonicArray(array):
    if len(array) <=2:
        return True
    i = 2
    j = 3
    mono = False
    while (i < len(array) and j < len(array)):
        if (array[i] <= array[j]):
            mono = True
            i+=1
            j += 1
        else:
            mono = False
            break

    while (i < len(array) and j < len(array)):
        if (array[j] <= array[i]):
            mono = True
            i+=1
            j += 1
        else:
            mono = False
            break
    return mono

print(monotonicArray([-1,-5,-10,-1100,-1100, -1101,-1102,-9001]))
