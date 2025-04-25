
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        dummy1, dummy2 = headA, headB

        while dummy1 != dummy2:
            dummy1 = dummy1.next if dummy1 else headB
            dummy2 = dummy2.next if dummy2 else headA

        return dummy1