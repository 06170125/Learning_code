
# Binary Search Tree 
● Binary Search Trees：樹的節點最多只有兩個子節點。 
    • 根節點（Root）：沒有父節點的節點是根節點。
      •右子樹：父節點右邊的樹。
      •左子樹：父節點左邊的樹。
    • 子節點（Leaf）：父節點下面的節點。
 

# ★ Search 搜尋


因為右子樹的值一定大於左子樹，所以只需從根節點開始比較，就知道搜尋值是位在右子樹或左子樹，然後再繼續往更下面的左子樹或右子樹進行比較，就可以找出是否擁有指定的節點值。

Step.1  
>先與根節點root進行比較


Step.2  
>如比root大，往右子樹查詢  
>如比root小，往左子樹查詢


Step.3  
>如果找得到，就回傳此值所在的位置  
>如果找不到，就回傳False



![Search 搜尋](https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/S__4136965.jpg?raw=true)

 

# ★ Insert 新增

觀念類似於「搜尋」,也就是比較後插入。我們只需從根節點開始比較，如要插入的數大於root，就往右；反之往左，然後繼續比較直到數值到達他應該待的位置為止。

Step.1  
>先與根節點root進行比較

Step.2  
>如比root大，往右子樹比較  
>如比root小，往左子樹比較
        
Step.3  
>如因比root小，所以往左子樹，那就再與左子樹的節點比較，小往左，大往右  
>如因比root大，所以往右子樹，那就再與右子樹的節點比較，小往左，大往右
        
Step.4  
>一直比較直到沒東西可以比，那便是此要新增的數值該在的地方。

![Insert 新增](https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/S__4136963.jpg?raw=true)

 

# ★Delete 刪除

對於一棵樹來說，刪除是較麻煩的事情，因為要設想出不同情況下的不同替換數。

●情況一：此節點無任何左、右子樹  
>解決方法：直接刪除

●情況二：此節點僅有左子樹  
>解決方法：從此節點僅有的左子樹中找出最大的點，然後替換上去

●情況三：此節點僅有右子樹  
>解決方法：從此節點僅有的右子樹中找出最小的點，然後替換上去

●情況四：此節點左、右子樹皆有  
>解決方法：  
>從此節點僅有的左子樹中找出最大的點，然後替換上去  
>從此節點僅有的右子樹中找出最小的點，然後替換上去

![Delete](https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/S__4136966.jpg?raw=true)

# ★修改

對於程式來說，他是把a值替換成b值，因為a不見了，而b新增了。但對於我們來說，修改就是先刪除再新增，因為我們會覺得將a換成b的是意思是連位置也一樣，可是現實卻不是，否則數可能會違反規定，所以我們只需要執行前面定義的「刪除」「新增」函數即可。

Step.1
>執行函數---刪除

Step.2
>執行函數---新增

![Modify 修改](https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/S__4136967.jpg?raw=true)

 

# ●資料來源：


<https://en.wikipedia.org/wiki/Binary_search_tree>

<https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture8.pdf？>

<https://courses.cs.washington.edu/courses/cse143/11wi/lectures/02-23/20-binary-search-t？ree.pdf>

<https://www.geeksforgeeks.org/deletion-binary-tree/> delete

<https://www.youtube.com/watch?v=bmaeYtlO2OE> insert

<https://en.wikipedia.org/wiki/Binary_search_tree> modify

<https://www.hackerearth.com/zh/practice/data-structures/trees/binary-search-tree/tutorial/> search


```python

```
