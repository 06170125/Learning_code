#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None
        elif l1 is not None and l2 is None:
            return l1
        elif l2 is not None and l1 is None:
            return l2

        l = []
        while l1 is not None:
            l.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l.append(l2.val)
            l2 = l2.next

        l = sorted(l)
        new_l = ListNode(l[0])
        head_l = new_l
        for i in range(1,len(l)):
            new_l.next = ListNode(l[i])
            new_l = new_l.next
        new_l.next = None
        return head_l


# In[ ]:




