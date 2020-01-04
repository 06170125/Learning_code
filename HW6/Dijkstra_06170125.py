#!/usr/bin/env python
# coding: utf-8

# In[39]:


from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.array = []
        self.roots = {}
    
    def addEdge(self,u,v,w): 
        if self.array == None:
            self.array.append([u,v,w])
            
        else:
            a = True
            for i in range(len(self.array)):
                if self.array[i][2] > w:
                    self.array.insert(i,[u,v,w])
                    a = False
                    break
            if a == True:
                self.array.append([u,v,w])

    def Kruskal_helper(self,end):
        
        point = self.array[0]

        if self.roots[point[0]] != None and self.roots[point[1]] != None and self.roots[point[0]] == self.roots[point[1]]:
            self.array.pop(0)
            point = self.array[0]
        
        self.array.remove(point)
        
        little = min(point[0],point[1])
        big = max(point[0],point[1])

        if self.roots[big] == None and self.roots[little] == None:
            self.roots[big] , self.roots[little] = little , little
            

        elif self.roots[big] == None and self.roots[little] != None:
            self.roots[big] = self.roots[little]
                      

        else:
            for i in range(self.V):
                if i != big and self.roots[i] == self.roots[big]:
                    self.roots[i] = little
            self.roots[big] , self.roots[little] = little , little

        end[str(str(point[0])+"-"+str(point[1]))] = point[2]

        if len(end) != self.V-1: self.Kruskal_helper(end)
            
        
        return end
    
    def Kruskal(self):
        for j in range(self.V): 
            self.roots[j] = None
        end = {}
        return self.Kruskal_helper(end)
    
    def Dijkstra(self, s):
        seen = [s]
        last = dict()
        past = dict()
        t = []
        for i in range(self.V):
            last[i] = None
            past[i] = None
        last[s] = 0
        for i in range(self.V-1):
            for x in range(len(self.graph[seen[-1]])):
                if self.graph[seen[-1]][x] != 0 and x not in seen:
                    val = self.graph[seen[-1]][x] + last[seen[-1]]
                    
                    if last[x] == None:
                        last[x] = val
                        past[x] = seen[-1]
                    else:
                        if val < last[x]:
                            last[x] = val
                            past[x] = seen[-1]
                    
                    if t == None:
                        t.append([x,last[x]])
                    else:
                        a  = True
                        for k in range(len(t)):
                            if t[k][1] > last[x]:
                                t.insert(k,[x,last[x]])
                                a = False
                                break
                        if a:
                            t.append([x,last[x]])
            
            while t[0][0] in seen:
                t.pop(0)
            seen.append(t[0][0])
            t.pop(0)
        
        final = {}
        for i in range(self.V):
            final[str(i)] = last[i]

        return final


# # 參考資料：
# https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_15
# 
# https://github.com/samuel871211/My-python-code/blob/master/HW6/Dijkstra_06170225.py
# 
# https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95
# 
# http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
# 
# http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
# 
# https://ithelp.ithome.com.tw/articles/10209593
# 
# https://www.itread01.com/content/1550267823.html

# In[ ]:




