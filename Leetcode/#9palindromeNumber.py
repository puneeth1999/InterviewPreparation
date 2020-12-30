'''
9. Palindrome Number
Easy

2876

1664

Add to List

Share
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1
'''
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    #dupliacte x
    x2 = x
    #reverse
    rev = 0
    while (x!=0):
        currDigit = x % 10
        x //= 10
        temp = rev*10 + currDigit
        rev = temp
    x = x2
    print(x, rev)
    #now, check
    if x == rev:
        return True
    return False