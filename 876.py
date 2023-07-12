

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        length=0
        if head.next is None:
            return(head)
        
        else:
            length += 1
            while curr.next is not None:
                curr = curr.next
                length+=1

            middle = (length // 2) + 1

            curr2 = head
            c=1
            while curr2.next is not None and c < middle:
                curr2 = curr2.next
                c += 1
            return (curr2)