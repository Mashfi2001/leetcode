# Definition for singly-linked list.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=ListNode()
        pot=head
        carry=0
        while l1 != None or l2 != None:
            if l1 != None and l2 == None:
                hold = l1.val+carry
                l1=l1.next
            elif l1 == None and l2 != None:
                hold = l2.val+carry
                l2=l2.next
            else:
                hold=(l1.val + l2.val)+carry
                l1=l1.next
                l2=l2.next
            digit=hold%10
            pot.next=ListNode(digit)
            pot=pot.next 
            if hold>9:
                carry=hold//10
            else:
                carry=0
        if carry!=0:
            pot.next=ListNode(carry)
        return head.next
        
            

        