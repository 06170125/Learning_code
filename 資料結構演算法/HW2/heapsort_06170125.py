{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#list -> tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#上面=largest\n",
    "#下面左=left 右=right\n",
    "#條件 = 上面必大於下面"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = [58,37,101,42,20,2,9,76,81]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#第一層是58，第二層左是37右是101，第三層左的左是42右是20 右的左是2右是9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = [0]\n",
    "a.extend([1,2,3])\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'a' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-72-82f326bc7c8e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minsert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'a' is not defined"
     ]
    }
   ],
   "source": [
    "a = \n",
    "c = [6]\n",
    "c.insert(0,a)\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "i = 0\n",
    "largest = nums[i] #最上面第0位\n",
    "left = nums[i+1]\n",
    "right = nums[(i+1)+1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(58, 37, 101)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "largest,left,right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = [58,37,101,42,20,2,9,76,81]\n",
    "nums.insert(0,nums[-1])\n",
    "\n",
    "i = 1\n",
    "largest = nums[i] #最上面第0位\n",
    "left = nums[i*2]\n",
    "right = (nums[i*2+1])\n",
    "\n",
    "new = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[81, 58, 37, 101, 42, 20, 2, 9, 76, 81]"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(58, 37, 101)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "largest,left,right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#狀況1.父節點小於子左節點  狀況2.父節點小於子右節點"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!!!!!重要!!!!!! 有幾個節點的運算方式 = n//2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "n = len(nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "while(left<=n and nums[left]>nums[largest]): #狀況1.\n",
    "    largest = left"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "while(right<=n and nums[right]>nums[largest]): #狀況2.\n",
    "    largest = right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "if largest != nums[i]:\n",
    "    nums[largest],nums[i] = nums[i],nums[largest]\n",
    "    new.append(nums[i])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "###合併"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'left' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-987e26e575b0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mright\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m \u001b[1;32mwhile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m<=\u001b[0m\u001b[0mn\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m>\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlargest\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m     \u001b[0mlargest\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;32mwhile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mright\u001b[0m\u001b[1;33m<=\u001b[0m\u001b[0mn\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mright\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m>\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mlargest\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'left' is not defined"
     ]
    }
   ],
   "source": [
    "#初稿\n",
    "nums = [58,37,101,42,20,2,9,76,81]\n",
    "def maxheapify(nums,n,i):\n",
    "    largest = i\n",
    "    left = (2*i+1)\n",
    "    right = (2*i)+2\n",
    "\n",
    "while(left<=n and nums[left]>nums[largest]):\n",
    "    largest = left,\n",
    "while(right<=n and nums[right]>nums[largest]):\n",
    "    largest = right\n",
    "if largest != i:\n",
    "    new.append(nums[i])\n",
    "    nums[largest],nums[i] = nums[i],nums[largest]\n",
    "    nums.pop(nums[i])\n",
    "    \n",
    "for i in n/2,i>1:\n",
    "    heapify(nums,n,i)\n",
    "\n",
    "nums[0],nums[i] = nums[i],nums[0]\n",
    " \n",
    "maxhepify(nums,n,i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution(object):\n",
    "    def heap_sort(self,nums):\n",
    "        nums.insert(0,0)\n",
    "\n",
    "        i = 1\n",
    "        n = len(nums)\n",
    "        largest = nums[i] #最上面第1位\n",
    "        left = nums[i*2] #左邊為第一位*2\n",
    "        right = (nums[i*2+1])#右邊是左邊加一位\n",
    "        new = []\n",
    "        \n",
    "        for i in range(n//2): #要計算n/2的整數次\n",
    "            while(left < n and nums[left]>nums[largest]): #當狀況一發生\n",
    "                largest = left #最大變為左\n",
    "            while(right < n and nums[right]>nums[largest]): #當狀況二發生\n",
    "                largest = right #最大為最右\n",
    "            if largest != nums[i]: #最大不等於第一位\n",
    "                nums[largest],nums[i] = nums[i],nums[largest] #交換\n",
    "                new.append(nums[i]) #增加新數字到new\n",
    "                nums.pop(nums[i]) #刪除他\n",
    "    def heap_Sort(nums): \n",
    "        n = len(nums) \n",
    "  \n",
    "        for i in range(n, -1, -1): \n",
    "            heapify(nums, n, i) \n",
    "  \n",
    "        for i in range(n-1, 0, -1): \n",
    "            nums[i], nums[1] = nums[1], nums[i]   # swap \n",
    "            heapify(nums, i, 0)\n",
    "        return new"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-105-1c37848ba63e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mnums\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m58\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m37\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m101\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m42\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m20\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m9\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m76\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m81\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0moutput\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSolution\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mheap_sort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnew\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-104-8ed2c7d93de7>\u001b[0m in \u001b[0;36mheap_sort\u001b[1;34m(self, nums)\u001b[0m\n\u001b[0;32m      6\u001b[0m         \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m         \u001b[0mlargest\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;31m#最上面第1位\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m         \u001b[0mleft\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;31m#左邊為第一位*2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m         \u001b[0mright\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mnums\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;31m#右邊是左邊加一位\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m         \u001b[0mnew\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "nums = [58,37,101,42,20,2,9,76,81]\n",
    "output = Solution().heap_sort(new)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#還是錯...我會繼續改..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=[1,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "data = [1,2,3,4,5,6,7,8,9,10]\n",
    "def heapsort(data):\n",
    "    i=len(data)//2-1\n",
    "    \n",
    "    while i>=0:\n",
    "        if 2*i+2 not in range(len(data)-1):\n",
    "            if data[i]<=data[2*i+1]:\n",
    "                data[i],data[2*i+1]=data[2*i+1],data[i]\n",
    "                i-=1\n",
    "            else:\n",
    "                i-=1\n",
    "        else:\n",
    "            if data[2*i+1]<data[2*i+2]:\n",
    "                    data[i]<=data[2*i+2]\n",
    "                    data[i],data[2*i+2]=data[2*i+2],data[i]\n",
    "                    i-=1\n",
    "                    \n",
    "            elif data[2*i+1]>data[2*i+2]:\n",
    "                data[i]<=data[2*i+1]\n",
    "                data[i],data[2*i+1]=data[2*i+1],data[i]\n",
    "                i-=1\n",
    "            else:\n",
    "                i-=1\n",
    "    heapsort(data)\n",
    "\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"
     ]
    }
   ],
   "source": [
    "nums = [1,2,3,4,5,6,7,8,9,10]\n",
    "class Solution(object):\n",
    "     def heap_sort(self,nums):\n",
    "        i=len(nums)//2-1\n",
    "        \n",
    "        while i>=0: #當i>0\n",
    "            if 2*i+2 not in range(len(nums)-1): #如果子右節點不存在\n",
    "                if nums[i]<=nums[2*i+1]: #就比較子左節點跟父節點\n",
    "                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #成立及交換\n",
    "                    i-=1 #i=i-1\n",
    "                else:#其他\n",
    "                    i-=1 #i=i-1\n",
    "            else:#如果子右存在\n",
    "                if nums[2*i+1]<nums[2*i+2]: #子左大於子右\n",
    "                        nums[i]<=nums[2*i+2] #父小於子右\n",
    "                        nums[i],nums[2*i+2]=nums[2*i+2],nums[i] #交換\n",
    "                        i-=1 #i=i-1\n",
    "                    \n",
    "                elif nums[2*i+1]>nums[2*i+2]: #子左大於子右\n",
    "                    nums[i]<=nums[2*i+1] #父小於子左\n",
    "                    nums[i],nums[2*i+1]=nums[2*i+1],nums[i] #交換\n",
    "                    i-=1 #i=i-1\n",
    "                else:\n",
    "                    i-=1 #i=i-1\n",
    "        heapsort(nums) #nums heapsort\n",
    "print(nums)"
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
