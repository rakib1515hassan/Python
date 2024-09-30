"""
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
"""

##! First, let's define the ListNode class to represent each node in the linked list:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



##! Now we can implement the solution that adds two numbers stored as linked lists:
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Create a dummy head to simplify handling of edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Loop through both lists as long as there are elements in l1 or l2
        while l1 or l2:
            # If l1 or l2 is None, use 0 as its value
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in the lists if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # If there's still a carry left at the end, create a new node
        if carry:
            current.next = ListNode(carry)

        # Return the result list, starting from the node after the dummy head
        return dummy_head.next


##! Helper Function to Convert List to Linked List:
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next


##! Helper Function to Convert Linked List to List:
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result



##! Define l1 and l2 as lists
l1 = [2, 4, 3]
l2 = [5, 6, 4]

# Convert them to linked lists
l1_linked = list_to_linkedlist(l1)
l2_linked = list_to_linkedlist(l2)

# Instantiate the solution and call the method
solution = Solution()
result_linked = solution.addTwoNumbers(l1_linked, l2_linked)

# Convert the result linked list back to a list for easy viewing
result = linkedlist_to_list(result_linked)
print(result)  # Output: [7, 0, 8]
