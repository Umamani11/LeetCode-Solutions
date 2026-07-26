# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head=ListNode()
        temp1,temp2,temp3=l1,l2,head
        while(temp1 is not None and temp2 is not None):
            if temp1.val<=temp2.val:
                temp3.next=temp1
                temp1=temp1.next
            else:
                temp3.next=temp2
                temp2=temp2.next
            temp3=temp3.next
        if(temp1 is not None):
            temp3.next=temp1
        if(temp2 is not None):
            temp3.next=temp2
        head=head.next
        return head
        
        