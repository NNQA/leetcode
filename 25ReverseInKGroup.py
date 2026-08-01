class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


def build_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head

        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        print("tail", tail)

        def reverse(cur, end):
            prev = None

            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev

        new_head = reverse(head, tail)
        print("new_head", new_head)
        head.next = self.reverseKGroup(tail, k)
        return new_head


sol = Solution()
list1 = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sol.reverseKGroup(list1, 2))
