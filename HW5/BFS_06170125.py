#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 
        
    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
    def BFS(self, s):
        Take = [] #一定要設定QAQ
        
        queue = [] #先設定一個丟暫時答案的地方
        queue.append(s) #把起始點s丟進去，把值一個一個丟進去

        search = [] #然後設定一個也是丟暫時答案，但是不會被pop的地方
        search.append(s) #把起始點s丟進去，把值一個一個丟進去，但是不會被pop
    
        while (len(queue) > 0): #如果長度大於0(小於0就不用找了)
            take = queue.pop(0) #拿出queue的東西，先進先出，所以pop(0)
            near_point = self.graph[take] #查詢take所有的鄰近點
            for x in near_point: #x是所有的鄰近點
                if x not in search: #x不在queue裡面的話
                    queue.append(x) #queue就會加入x
                    search.append(x) #同時search也會加入，但不會被拿出，所以才要做為查詢
            Take.append(take)#要加進去
        return Take #Take就是我的答案

    def DFS(self, s):
        Take = [] #一定要設定QAQ
        
        stack = [] #先設定一個丟暫時答案的地方
        stack.append(s) #把起始點s丟進去，把值一個一個丟進去

        search = []#然後設定一個也是丟暫時答案，但是不會被pop的地方
        search.append(s)#把起始點s丟進去，把值一個一個丟進去，但是不會被pop
    
        while (len(stack) > 0): #如果長度大於0(小於0就不用找了)
            take = stack.pop(-1) #拿出queue的東西，先進先出，所以pop(0)
            near_point = self.graph[take] #查詢take所有的鄰近點
            for y in near_point: #y是所有的鄰近點
                if y not in search: #y不在stack裡面的話
                    stack.append(y) #stack就會加入y
                    search.append(y) #同時search也會加入，但不會被拿出，所以才要做為查詢
            Take.append(take)#要加進去
        return(Take) #Take就是我的答案


# # 參考資料

# https://www.programiz.com/dsa/graph-bfs
# 
# https://www.twblogs.net/a/5c8ae7f8bd9eee35cd6aa6d5
# 
# https://hackmd.io/@cube/SysqQALcN
# 
# https://csie.ntnu.edu.tw/~u91029/Graph.html
# 
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# 
# https://blog.csdn.net/g11d111/article/details/76169861
