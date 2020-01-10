#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def isAlienSorted(self, words, order):
        alien_dic = {}
        # create alien dictionary by using enumerate
        for i, c in enumerate(order):
            alien_dic[c] = i

        dic_order = sorted(words, key=lambda x: [alien_dic[c] for c in x])
        return dic_order == words


# In[ ]:




