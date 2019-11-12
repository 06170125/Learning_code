{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-3, 0, 4, 5, 39, 73, 84]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nums = [4,73,5,0,-3,84,39] #我設定的nums\n",
    "new=[] #新的list\n",
    "class Solution(object):  #規定格式\n",
    "    def heapsort(nums): #定義一個heapsort函數\n",
    "        i=len(nums)//2-1 # i是父節點，最後的父節點是長度除二的整數位減一\n",
    "        while i>=0: #如果父節點大於0才執行\n",
    "            if 2*i+2 > len(nums)-1: #狀況一:沒有子右節點\n",
    "                while nums[i]<=nums[2*i+1]:#如果父節點小於子左節點\n",
    "                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #交換\n",
    "                i-=1 #i後退一個，新的父節點出現\n",
    "            else: #狀況二:有左右兩個節點\n",
    "                while nums[i]<=nums[2*i+1]: # 如果父節點小於等於子左節點\n",
    "                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #交換\n",
    "                while nums[i]<nums[2*i+2]: #如果父節點小於子右節點\n",
    "                    nums[i],nums[2*i+2]=nums[2*i+2],nums[i] #交換\n",
    "                i-=1 #i後退一個，新的父節點出現\n",
    "        nums[0],nums[-1]=nums[-1],nums[0] #第一位與最後一位交換\n",
    "        new.append(nums[-1]) #新的list增加一個nums的末位數\n",
    "        nums.pop(-1) # 讓nums的末位不見\n",
    "    while len(nums)>0: #當nums長度大於0\n",
    "        heapsort(nums) #執行heapsort\n",
    "    list(reversed(new)) #list改成由小到大的樣子\n",
    "output = list(reversed(new)) #老師規定的格式\n",
    "output #print出來"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
