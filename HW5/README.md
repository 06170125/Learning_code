# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About BFS

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>從起點開始搜尋與自己相鄰相近的點
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>每找到新的資料，以Queue的方式儲存並取出，取出之點不能重複。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>依此類推，直至資料取出完畢
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>因此資料存取的順序是先進先出，越先存入的資料，取出優先順序反而越前面，類似我們現實中所謂的排隊。
>


# <img width="30" height="30" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E6%84%9B%E5%BF%83.png?raw=true"/> About DFS

><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>將資料存進堆疊，從頂端依序放置底端，取出時只能從頂端拿
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>故資料存取的順序是先進後出，也就是說，越先存入堆疊的資料，取出優先順序反而越後面。
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>通常是以遞迴的方式呈現
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>不斷的往深處進去，直到沒有子節點，再折返回來
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>換進去其他深處，對於深度低的狀態空間來說，不但相當簡潔，所占用的空間記憶體也較少，執行上的效率也跟著快
>
><img width="15" height="15" src="https://github.com/06170125/Learning_code/blob/master/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E6%BC%94%E7%AE%97%E6%B3%95/%E8%97%8D%E7%AE%AD%E9%A0%AD.png?raw=true"/>但相對的，深度過深的話，對電腦的負荷也相當的大
>

