#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class MyHashSet:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        
        
    def md5(self,key): #透過md5轉成雜湊值，所以我先設定一個md5函數
        h=MD5.new()
        h.update(key.encode("utf-8"))
        hashnum=h.hexdigest()
        hashnum=int(h.hexdigest(), 16)
        ind=hashnum % self.capacity
        return ind
        
    def add(self, key): #新增
        new = ListNode(key) #新的節點
        ind = self.md5(key) #經過md5函數的數值
        if self.contains(key) == True: #如果這個數值已經存在的話
            return #直接回傳，因為list中同樣數值存在一次就好
        if self.contains(key) != True: #如果數值不存在
            if self.data[ind] == None: #如果list沒東西，也就是加進來的東西為第一個
                self.data[ind] = new #那他就是新的
            else: #其他，如果list有東西(衝突)
                num = self.data[ind] 
                while (num.next): 
                    num = num.next #跳下個，直到沒下個
                num.next = new #就可以加了
                
    def remove(self, key): #刪除
        ind = self.md5(key) #經過md5函數的數值
        num = self.data[ind] 
        none = None
        if num and key != num.data: #如果要刪的東西根本不存在
            none=num
            num=num.next
        
        if num is None: #沒數值
            return #直接回傳
        if none is None:
            self.data[ind] = self.data[ind].next
        else:
            none.next = num.next
            
    def contains(self, key): #查詢
        ind=self.md5(key) #經過md5函數的數值
        num = self.data[ind]
        if num == None: #如果查詢東西不存在
            return False
        if num.data == key: #如果查詢東西剛好等於第一數
            return True
        if num.next: #如果查詢的東西是節點
            while (num.next) != None: #下一位不適空值
                num=num.next #往下一位繼續查
                if num.data == key: #查到就true
                    return True
                if num.data != key: #查不到就false
                    False
        else:
            return False   


# # 參考資料

# https://www.cs.wcupa.edu/rkline/ds/hash-sets.html
# 
# 
# https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/
# 
# 
# https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g790b8351ca_0_114
# 
# 
# https://www.itread01.com/content/1541332933.html
#     
#     
# https://medium.com/@fchern/%E8%A8%AD%E8%A8%88%E9%AB%98%E6%95%88%E8%83%BD%E7%9A%84hash-table-%E4%B8%80-303d9713abab
#     
# 
# https://carlos-studio.com/2018/01/21/%E6%BC%94%E7%AE%97%E6%B3%95-%E9%9B%9C%E6%B9%8A%E8%A1%A8hash-table/

# In[ ]:




