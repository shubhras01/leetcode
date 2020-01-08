# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def get_mid(self, head):
        if not head:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l1, l2):
        prehead = ListNode(float('-Inf'))
        curr = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prehead.next = l1
                l1 = l1.next
            else:
                prehead.next = l2
                l2 = l2.next
            prehead = prehead.next
        while l1:
            prehead.next = l1
            l1 = l1.next
            prehead = prehead.next
        while l2:
            prehead.next = l2
            l2 = l2.next
            prehead = prehead.next

        return curr.next

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        mid_next = mid.next
        # print head.val, mid.val, mid_next.val
        mid.next = None

        l1 = self.merge_sort(head)
        l2 = self.merge_sort(mid_next)
        sorted_l = self.merge(l1, l2)
        return sorted_l

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge_sort(head)

    def printList(self, head):
        while head:
            print str(head.val) + " --> ",
            head = head.next

if __name__ == "__main__":
    arr = [4,2,1,3]
    prehead = ListNode(float('-Inf'))
    tmp = prehead
    for i in arr:
        curr = ListNode(i)
        prehead.next = curr
        prehead = prehead.next

    s = Solution()
    head = s.sortList(tmp.next)
    s.printList(head)


