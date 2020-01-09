# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About Merge Sort

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>合併排序法(或稱歸併排序法)，是排序演算法的一種
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>使用Divide and Conquer的演算法來實作。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>排序時需要額外的空間來處理
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.1 將陣列分割直到只有一個元素
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.2 開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.3 重複STEP.2的動作直到全部合併完成。

# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About Heap Sort

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>二元樹的一種 ⇒ 每個父節點最多兩個子節點
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>堆積樹為完全二元樹的一種。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>最小堆積(Min Heap)：父節點的值小於子節點
樹根(root)一定最所有節點的最小值
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>最大堆積(Max Heap)：父節點的值大於子節點
樹根(root)一定最所有節點的最大值
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.1 我們會先將陣列轉換成Heap Tree
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.2 從最後的父節點，開始進行Max Heap判斷，然後再往前遞回
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.3 再往回前一個父節點
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.4 再來判斷root
