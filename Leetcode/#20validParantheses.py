'''
20. Valid Parentheses
Easy

6349

262

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
def isValid(self, s: str) -> bool:
    dic = {'[': ']', '(': ')', '{': '}'}
    stack = []

    #if the string starts with a closing bracket, then the string is not valid
    if s[0] not in dic:
        return False

    #Checking remaining elements in the string
    for x in s:

        #if there is nothoing to compare it to, then the string won't be valid
        if (x in dic):
            stack.append(x)
        else:
            if len(stack) <= 0:
                return False
            temp = stack.pop()
            if dic[temp] is x:
                continue
            else:
                return False
    if len(stack) is 0:
        return True
    return False
