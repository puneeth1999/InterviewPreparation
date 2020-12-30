'''
2. Add Two Numbers
Medium

10130

2536

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    numString1 = ""
    numString2 = ""

    #List1
    current = l1
    while(current != None):
        numString1 += str(current.val)
        current = current.next

    #List2
    current = l2
    while(current != None):
        numString2 += str(current.val)
        current = current.next

    numString1 = numString1[::-1]
    numString2 = numString2[::-1]

    num1 = int(numString1)
    num2 = int(numString2)
    print('num1:', num1, 'num2:', num2)
    sum1 = num1 + num2
    print('sum1:', sum1)
    resultString = str(sum1)
    resultString = resultString[::-1]

    lister = list(resultString)
    finalList = [int(k) for k in lister]
    print(lister)
    print(finalList)

    # curr = l1
    # for k in finalList:
    #     curr.val = k
    #     curr = curr.next

    newList = ListNode()
    curr = newList
    # for k in finalList:
    #     curr.val = k
    #     curr.next = ListNode()
    #     curr = curr.next
    print('the iterations start here:')
    k = 0
    for k in range(len(finalList) - 1):
        curr.val = finalList[k]
        print(finalList[k])
        curr.next = ListNode()
        curr = curr.next
    if(len(finalList) > 1):
        curr.val = finalList[k+1]
        print(finalList[k+1])
    if(len(finalList) == 1):
        curr.val = finalList[0]
    return newList
