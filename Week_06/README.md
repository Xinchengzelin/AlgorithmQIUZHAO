学习笔记

# 学习总结
## 用自己熟悉的编程语言，手写各种初级排序代码，提交到学习总结中。
- 1、冒泡排序-代码最简单,将最大的元素依次放到后面（也可以将最小的元素放到最前面）
```
class Solution:
    def Sort(self,arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1],arr[j] = arr[j],arr[j+1]
        print(arr)
```
- 2、选择排序-找到最小值，放在最前面
```
class Solution:
    def Sort(self,arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i,len(arr)):
                if arr[minIndex] > arr[j]:
                    minIndex = j
            arr[minIndex],arr[i] = arr[i],arr[minIndex]
        print(arr)
```
- 3、插入排序-将剩余元素逐步插入前面的排序数组中
```
class Solution:
    def Sort(self,arr):
        for i in range(1,len(arr)):
            key = arr[i]#key是拿出排序的元素
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key#注意是j+1 
        print(arr)
```
- 4、快速排序 - 分治，直接修改数组in place
```
class Solution:            
    def Sort(self,begin,end,arr):
        if begin >= end:
            return
        pivot_index = self.partion(begin,end,arr)
        self.Sort(begin,pivot_index-1,arr)
        self.Sort(pivot_index+1,end,arr)
        print(arr)

    def partion(self,begin,end,num):
        pivot=end #标杆位置
        counter = begin #小于标杆的个数
        for i in range(begin,end):
            if num[i] < num[pivot]:
                num[i],num[counter] = num[counter],num[i]
                counter += 1
        num[pivot],num[counter] = num[counter],num[pivot]#pivot_index前面都小于，后面都大于等于
        return counter
```
- 5、归并排序 - 分成两个长度n/2的序列，然后分别排序（递归排序），最后合并
```
class Solution:            
    def Sort(self,left,right,arr):
        if left >= right:
            return
        mid = (left + right) >> 1
        self.Sort(left,mid,arr)
        self.Sort(mid+1,right,arr)
        self.merge(left,right,mid,arr)
    def merge(self,left,right,mid,arr):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        arr[left:right+1] = temp
        print(arr)
```
- 6、堆排序 
```
import heapq
class Solution:            
    def Sort(self,arr):
        if not arr: return []
        heap = heapq.heapify(arr)
        print([heapq.heappop(arr) for _ in range(len(arr))])
```
- 测试
```
Solution().Sort([])
Solution().Sort([2, 8, 7, 4, 6, 3,6])
Solution().Sort([12,4,132,55,46,232,789,1,0,98,523,666])
# 快排/归并测试
# Solution().Sort(0,0,[])
# Solution().Sort(0,6,[2, 8, 7, 4, 6, 3,6])
# Solution().Sort(0,11,[12,4,132,55,46,232,789,1,0,98,523,666])
```
## 在学习总结中，写出不同路径 2 这道题目的状态转移方程（选学）。



# 经典代码
- 一句话替代if……elif……else
```
res = sign * res
if res >= 2**31 -1:
    return 2**31 -1
elif res <= -2**31:
    return -2**31
else:
    return res
```
可以直接用下面的代码替代
```
return min(2**31-1,max(res * sign,-2**31))
```
- for……else的使用
break后会执行else里的内容

# 题目要点
- 字符串处理的题目一不小心会写的很复杂，如果需要修改字符串，很多时候要转成list

- Python字符串是immutable，所以字符串问题要么转化成list在修改解决，要么增加一个res的结果list储存结果

- 注意下面两行代码的运行区别
```
print("".split())#[]#注意运行结果
print("".split(" "))#['']
```
# 题目记录