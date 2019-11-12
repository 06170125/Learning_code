#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = [4,73,5,0,-3,84,39] #我設定的nums
new=[] #新的list
class Solution(object):  #規定格式
    def heapsort(nums): #定義一個heapsort函數
        i=len(nums)//2-1 # i是父節點，最後的父節點是長度除二的整數位減一
        while i>=0: #如果父節點大於0才執行
            if 2*i+2 > len(nums)-1: #狀況一:沒有子右節點
                while nums[i]<=nums[2*i+1]:#如果父節點小於子左節點
                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #交換
                i-=1 #i後退一個，新的父節點出現
            else: #狀況二:有左右兩個節點
                while nums[i]<=nums[2*i+1]: # 如果父節點小於等於子左節點
                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #交換
                while nums[i]<nums[2*i+2]: #如果父節點小於子右節點
                    nums[i],nums[2*i+2]=nums[2*i+2],nums[i] #交換
                i-=1 #i後退一個，新的父節點出現
        nums[0],nums[-1]=nums[-1],nums[0] #第一位與最後一位交換
        new.append(nums[-1]) #新的list增加一個nums的末位數
        nums.pop(-1) # 讓nums的末位不見
    while len(nums)>0: #當nums長度大於0
        heapsort(nums) #執行heapsort
    list(reversed(new)) #list改成由小到大的樣子
output = list(reversed(new)) #老師規定的格式
output #print出來


# In[ ]:




