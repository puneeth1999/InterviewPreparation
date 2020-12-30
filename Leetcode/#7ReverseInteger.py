'''
7. Reversed Integer
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
'''
def reverse(self, x: int) -> int:
    if(len(str(x)) < 2):
        return x

    neg = False
    if(x < 0):
        x = -x
        neg = True
    stack = []
    while(x != 0):
        currentLastDigit = x % 10
        x //= 10
        stack.append(currentLastDigit)
    s = ""
    for i in stack:
        s += str(i)
    print(s)

    if(int(s) >= 2**31 - 1 or int(s) <= -2**31):
        return 0
    if neg == True:
        return -int(s)
    return int(s)
