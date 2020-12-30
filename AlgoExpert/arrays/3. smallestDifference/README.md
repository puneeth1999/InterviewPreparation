# Smallest Difference
### Problem Statement:
Two arrays are given and we need to find an two elements - one from each array such that the difference between those two numbers are as least as possible.

### Solution
There are two approaches. One approach is straight forward which involves two for loops which makes it O(n^2).
Another one is using two indices.
1. Sort two arrays
2. Take pointers and point them to the zeroth position of the arrays.
3. We need to bring those elements as close as possible. So, if(firstNum < secondNum), idxOne += 1. Else, vice versa.
