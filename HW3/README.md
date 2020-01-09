# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About Merge Sort

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>Binary Search Trees：樹的節點最多只有兩個子節點。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>根節點（Root）：沒有父節點的節點是根節點。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>右子樹：父節點右邊的樹。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>左子樹：父節點左邊的樹
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>子節點（Leaf）：父節點下面的節點。
>

# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E4%BA%AE%E6%99%B6%E6%99%B6.png?raw=true"/> 搜尋
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>因為右子樹的值一定大於左子樹，所以只需從根節點開始比較，就知道搜尋值是位在右子樹或左子樹，然後再繼續往更下面的左子樹或右子樹進行比較，就可以找出是否擁有指定的節點值。


>
# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E4%BA%AE%E6%99%B6%E6%99%B6.png?raw=true"/> 新增
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>觀念類似於「搜尋」,也就是比較後插入。我們只需從根節點開始比較，如要插入的數大於root，就往右；反之往左，然後繼續比較直到數值到達他應該待的位置為止
>
# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E4%BA%AE%E6%99%B6%E6%99%B6.png?raw=true"/> 刪除
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>對於一棵樹來說，刪除是較麻煩的事情，因為要設想出不同情況下的不同替換數。
>
# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E4%BA%AE%E6%99%B6%E6%99%B6.png?raw=true"/> 修改
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>對於程式來說，他是把a值替換成b值，因為a不見了，而b新增了。但對於我們來說，修改就是先刪除再新增，因為我們會覺得將a換成b的是意思是連位置也一樣，可是現實卻不是，否則數可能會違反規定，所以我們只需要執行前面定義的「刪除」「新增」函數即可。。
