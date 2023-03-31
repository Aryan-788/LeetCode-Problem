# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        node1, node2 = l1, l2
        while node1 is not None:
            num1 = str(node1.val) + num1
            node1 = node1.next
        while node2 is not None:
            num2 = str(node2.val) + num2
            node2 = node2.next
        num1 = int(num1)
        num2 = int(num2)
        summ = num1 + num2
        summ = str(summ)
        
        digitnodes = list(summ)
        
        for idx, digit in enumerate(summ):
            if idx == 0:
                digitnodes[idx] = ListNode(val = digit, next=None)
            else: 
                digitnodes[idx] = ListNode(val = digit, next=digitnodes[idx-1])
            
        
        return(digitnodes[len(digitnodes)-1])  
