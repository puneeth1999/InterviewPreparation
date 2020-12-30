'''
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.



Example

For n = 2, the output should be
shapeArea(n) = 5;
For n = 3, the output should be
shapeArea(n) = 13.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n < 104.

[output] integer

The area of the n-interesting polygon.
'''
def shapeArea(n):
    counter = 1
    middle_strip = 1
    shape = 0
    if(n>1):
        #to find the middle strip area
        while(counter < n):
            middle_strip += 2
            counter += 1
        shape = 1
        s_shape = 1
        counter = 1
        #to find the area of other strips on one side
        while(counter < n-1):
            s_shape += 2
            counter += 1
            shape += s_shape
        shape *= 2
    return middle_strip + shape

print(shapeArea(5))
