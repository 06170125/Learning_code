# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About Dijkstra

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>主要內容是指定一個點 (原點) 到其餘各個頂點的最短路徑，也稱作「最短路徑」
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.1 至起始點找尋尚未拜訪的相鄰結點
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.2 加到queue
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.3 找尋目前未拜訪的最短路徑結點，將此結點設為起始點，並設為已拜訪。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.4 重複第一步，直到所有結點皆為已拜訪。


# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About Krustal

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>此演算法是一種用來尋找最小生成樹的演算法
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.1 將每個頂點放入其自身的資料集合中
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.2 按照權值的升序來選擇邊
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.3 當選擇每條邊時，判斷定義邊的頂點是否在不同的資料集中
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.4 如果是，將此邊插入最小生成樹的集合中，同時，將集合中包含每個頂點的聯合體取出
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E7%B6%A0%E7%AE%AD%E9%A0%AD.png?raw=true"/>STEP.5 如果不是，就移動到下一條邊。重複這個過程直到所有的邊都探查過
