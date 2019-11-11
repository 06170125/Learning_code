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
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "#分割 -> 排序 -> 合併"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = [10,9,8,7,6,5,4,3,2,1,11]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#分割"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "#分成一半\n",
    "\n",
    "a = x[:len(x)//2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 9, 8, 7, 6]"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "b = x[len(x)//2:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 4, 3, 2, 1, 11]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "# x -> a,b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = [10,9,8,7,6,5,4,3,2,1,11]\n",
    "def devide(x):\n",
    "    if len(x) <= 1:\n",
    "        return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "#再分\n",
    "a = devide(x[:len(x)//2])\n",
    "b = devide(x[len(x)//2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_sort(self,nums):\n",
    "    if len(nums) > 1:\n",
    "            \n",
    "        a = nums[:len(nums)//2]\n",
    "        b = nums[len(nums)//2:]\n",
    "            \n",
    "        Solution().merge_sort(a)\n",
    "        Solution().merge_sort(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "#排序"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-66-d00c5981b777>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-66-d00c5981b777>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    c.append(a[i]):\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "i = 0\n",
    "j = 0\n",
    "c = []\n",
    "\n",
    "if a[i] < b[j]:\n",
    "    c.append(a[i]):\n",
    "    i += 1\n",
    "    \n",
    "else:\n",
    "    c.append(b[j]):\n",
    "    j += 1\n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'c' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-67-652ac1b71da3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[0mi\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mj\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m         \u001b[0mc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m         \u001b[0mi\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'c' is not defined"
     ]
    }
   ],
   "source": [
    "a = [2,3]\n",
    "b = [6,1]\n",
    "def sort(a,b):\n",
    "    i = 0\n",
    "    j = 0\n",
    "    c = []\n",
    "    \n",
    "while i < len(a) and j < len(b):\n",
    "    if a[i] < b[j]:\n",
    "        c.append(a[i])\n",
    "        i += 1\n",
    "        \n",
    "    else:\n",
    "        c.append(b[j])\n",
    "        j += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-68-2988d9917c21>, line 18)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-68-2988d9917c21>\"\u001b[1;36m, line \u001b[1;32m18\u001b[0m\n\u001b[1;33m    i += 1\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "a = [2,3]\n",
    "b = [6,1]\n",
    "\n",
    "i = 0\n",
    "j = 0 \n",
    "k = 0\n",
    "            \n",
    "while i < len(a) and j < len(b):\n",
    "    if a[i] < b[j]:\n",
    "        x[k] = a[i]\n",
    "        i += 1\n",
    "    else:\n",
    "        x[k] = b[j]\n",
    "        j += 1\n",
    "    k += 1\n",
    "while i < len(a):\n",
    "    nums[k] = a[i]\n",
    "        i += 1\n",
    "        k += 1\n",
    "                \n",
    "while j < len(b):\n",
    "        nums[k] = b[j]\n",
    "        j += 1\n",
    "        k += 1\n",
    "        return nums           \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "############################################################################"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution(object):   \n",
    "    def merge_sort(self,nums): #定義一個名為mergesort的函數，我輸入的東西叫做nums\n",
    "        if len(nums) <= 1: #如果我輸入的nums長度小於等於1\n",
    "            return nums #直接回傳nums\n",
    "        if len(nums) > 1: #如果我輸入的nums長度大於1，跑出函數\n",
    "            \n",
    "            a = nums[:len(nums)//2] #a是左邊的list，範圍是nums裡面\n",
    "            b = nums[len(nums)//2:] #b是左邊的list，範圍是nums裡面\n",
    "            \n",
    "            Solution().merge_sort(a) #左邊的list再繼續作左右之分\n",
    "            Solution().merge_sort(b) #右邊的list再繼續作左右之分\n",
    "            \n",
    "            i = 0 \n",
    "            j = 0\n",
    "            k = 0\n",
    "            \n",
    "            while i < len(a) and j < len(b): #當a的長度大於i(這裡的i會用在a)然後當b的長度大於j(這裡的j會用在b)\n",
    "                if a[i] < b[j]: #如果a裡面的第一個數字小於b裡面的第一個數字\n",
    "                    nums[k] = a[i] #nums裡面的第k位(也就是第0位)就會等於a的第一位\n",
    "                    i += 1 #然後 i = i+1\n",
    "                else: #其他\n",
    "                    nums[k] = b[j] #nums裡面的第k位(也就是第0位)就會等於b的第一位\n",
    "                    j += 1 #然後 j = j+1\n",
    "                k += 1 # k=k+1(這邊k要對齊迴圈)\n",
    "            \n",
    "            while i < len(a): #當a的長度大於i(這裡的i會用在a)\n",
    "                nums[k] = a[i] #nums裡面的第k位，就會等於a的第一位\n",
    "                i += 1 #然後 i = i+1\n",
    "                k += 1 # k=k+1\n",
    "                \n",
    "            while j < len(b): #當b的長度大於j(這裡的j會用在b)\n",
    "                nums[k] = b[j] #nums裡面的第k位，就會等於b的第一位\n",
    "                j += 1 #然後 j = j+1\n",
    "                k += 1 # k=k+1\n",
    "            return nums #回傳數值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = [10,9,8,7,6,5,4,3,2,1,11 #我設定的nums\n",
    "\n",
    "output = Solution().merge_sort(nums) #規定的格式"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output"
   ]
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
