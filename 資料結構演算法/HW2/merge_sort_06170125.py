#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):   
    def merge_sort(self,nums): #定義一個名為mergesort的函數，我輸入的東西叫做nums
        if len(nums) <= 1: #如果我輸入的nums長度小於等於1
            return nums #直接回傳nums
        if len(nums) > 1: #如果我輸入的nums長度大於1，跑出函數
            
            a = nums[:len(nums)//2] #a是左邊的list，範圍是nums裡面
            b = nums[len(nums)//2:] #b是左邊的list，範圍是nums裡面
            
            Solution().merge_sort(a) #左邊的list再繼續作左右之分
            Solution().merge_sort(b) #右邊的list再繼續作左右之分
            
            i = 0 
            j = 0
            k = 0
            
            while i < len(a) and j < len(b): #當a的長度大於i(這裡的i會用在a)然後當b的長度大於j(這裡的j會用在b)
                if a[i] < b[j]: #如果a裡面的第一個數字小於b裡面的第一個數字
                    nums[k] = a[i] #nums裡面的第k位(也就是第0位)就會等於a的第一位
                    i += 1 #然後 i = i+1
                else: #其他
                    nums[k] = b[j] #nums裡面的第k位(也就是第0位)就會等於b的第一位
                    j += 1 #然後 j = j+1
                k += 1 # k=k+1(這邊k要對齊迴圈)
            
            while i < len(a): #當a的長度大於i(這裡的i會用在a)
                nums[k] = a[i] #nums裡面的第k位，就會等於a的第一位
                i += 1 #然後 i = i+1
                k += 1 # k=k+1
                
            while j < len(b): #當b的長度大於j(這裡的j會用在b)
                nums[k] = b[j] #nums裡面的第k位，就會等於b的第一位
                j += 1 #然後 j = j+1
                k += 1 # k=k+1
            return nums #回傳數值
        
nums = [10,9,8,7,6,5,4,3,2,1,11]#我設定的nums
output = Solution().merge_sort(nums) #規定的格式
output


# In[ ]:




