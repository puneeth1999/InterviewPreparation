# Longest Peak
### Problem Statement
An element in an array could be called a peak if the elements occuring before and after are less than itself.
<br/>
For Example,<br/>
Consider the following array.<br/>
[1,4,5,0,2]<br/>
In the array given above, there exists only one peak and that is:  5.<br/>
Since, the element occuring before (4) and the element occuring after (0) are less than 5.
<br/>
In this case, the ***length of the peak = 4***.<br/>Because on the left of the peak 5, the numbers till 1 are strictly decreasing.
<br/>
However, on the right side of the peak, after 0, the value starts raising again.<br/>
So, the peak constitutes [1,4,5,0].
### Solution
Think of this problem as a two part problem and merge it as one part later. (Check out the python files).
<br/>
Solving this problem basically contains 2 parts:
1. Identify all the peaks.
2. Calculate the length of each peak and update the value of the longest peak.
