#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val): #root=3
        if root!= None: #如果root找得到
            while val>root.val: #如果新增的數字大於root
                if root.right != None: #如果右子樹存在
                    return Solution().insert(root.right,val) #回傳繼續比較
                else: #如果右子樹不存在
                    return TreeNode(val) #就加在右邊
            while val<=root.val: #<=root往左
                if root.left != None: #如果左子樹存在
                    return Solution().insert(root.left,val) #回傳繼續比較
                else: #左子樹不存在
                    return TreeNode(val) #就加在左邊
        else: #如果root找不到
            root = TreeNode(val)
            return root
        
    def search(self,root,target):
        while root.val == target: #如果欲查詢值等於root
            root.val=target
            return root #直接回傳
        
        while root != target: #如果欲查詢值不等於root
            while target <= root.val: #預查值小於等於root
                if root.left != None: #左子數存在
                    return self.search(root.left,target) #回傳繼續比較
                else: #其他
                    return None #回傳none
                    
            while target > root.val: #如預查值大於root
                if root.right != None:#右子數存在
                    return self.search(root.right,target)#回傳繼續比較
                else: #其他
                    return None#回傳none
                
    def delete(self,root,target):
        top = None
        node = root
        
        while node and node.val == target: #如果欲查刪除值等於root
            return root #直接回傳
        
        while node and node.val != target:#如果欲刪除值不等於target
            top = node
            if target < node.val: #預查值小於node
                node = node.left #往左子樹走
            elif target > node.val: #預查值小於node
                node = node.right #往右子樹走
                
        #↑到底為甚麼這邊不能用while!!!#
                
        while node == None: #如果node沒有直
            return root #直接回傳
        while node.right == None and node.left == None: #狀況一：沒有左右子樹
            node = None #直接刪除
            if target <= top.val:
                top.left = node
            elif target > top.val:
                top.right = node
            return root
        
        while node.left != None and node.right == None: #狀況二：沒有右子樹
            if target < top.val:
                top.left = node.left
                return self.delete(root,target)
            else:
                top.right=node.right
                return self.delete(root,target)
            
        while node.right != None and node.left == None: #狀況三：沒有左子樹
            if target > top.val:
                top.right = node.right
                return self.delete(root,target)
            else:
                top.left=node.left
                return self.delete(root,target)
 
        while node.left != None and node.right != None: #狀況四：有左右子樹
            if target > top.val:
                top.right = node.right
                return self.delete(root,target)
            else:
                top.left=node.left
                return self.delete(root,target)
            
    def modify(self,root,target,new_val):
        root = self.delete(root,target)
        self.insert(root,new_val)
        return root


# # 參考資料

# https://en.wikipedia.org/wiki/Binary_search_tree
#     
# https://www.hackerearth.com/zh/practice/data-structures/trees/binary-search-tree/tutorial/
# 
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture8.pdf？
# 
# https://courses.cs.washington.edu/courses/cse143/11wi/lectures/02-23/20-binary-search-t？ree.pdf
# 
# https://www.geeksforgeeks.org/deletion-binary-tree/
# 
# https://www.youtube.com/watch?v=bmaeYtlO2OE
# 
# https://en.wikipedia.org/wiki/Binary_search_tree 
# 

# In[ ]:




