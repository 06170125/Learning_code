#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def removeElement(self, nums, val):
        if not len(nums):
            return 0

        i = 0
        while  i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i = i + 1
        
        return len(nums)


# In[ ]:




