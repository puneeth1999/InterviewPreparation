# THE TWO NUMBER SUM PROBLEM
### Problem Statement:
We get an array and a "target number". We need to find a pair of numbers whose sum would be equal to the given "target number"
#### There are 3 ways to do this.
1. Brute Force: We just take two for loops and solve the problem. But it takes O(n^2) time which is not enough. However the space complexity of this approach is O(1).
2. Two Pointer Method: We fist sort the array using any good sorting algo like MergeSort. Then, we take left and righ pointers, take the sum and compare the sum with the "target number" and act according to the result. This makes the time complexity O(nlogn) and space complexity O(1).
3. Using a HashTable. We can make the time complexity O(n) and space complexity O(n). Saves a lot of time. But maybe not suitable for systems with space constraints.
