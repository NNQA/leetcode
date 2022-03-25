# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_node = ListNode(val = (l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10
        currentNode = add_node
        
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            currentNode.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            currentNode = currentNode.next
        while(l1.next):
            l1 = l1.next
            currentNode.next = ListNode(val = (carry_over +l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            currentNode = currentNode.next
        while(l2.next):
            l2 = l2.next
            currentNode.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            currentNode = currentNode.next
        if(carry_over) > 0:
            currentNode.next = ListNode(val = 1)
        return(add_node)