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

