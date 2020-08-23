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
dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])

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
| 周次  | 类型   | 题目编号   | 题目                | 难度 | 分类        | 备注     | 第1次       |        | 第2次 |       | 第3次 |       | 方法                       |
|-----|------|--------|-------------------|----|-----------|--------|-----------|--------|-----|-------|-----|-------|--------------------------|
| KW6 | 周作业  | 146    | LRU 缓存机制          | 中等 | LRU Cache |        | 2020/8/17 | KW34/1 |     | KW0/6 |     | KW0/6 | 利用OrderedDict            |
| KW6 | 周作业  | 1122   | 数组的相对排序           | 简单 | 排序        |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 242取消  | 有效的字母异位词          | 简单 | 排序        |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 1244   | 力扣排行榜             |    | 排序        | plus会员 |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 56     | 合并区间              | 中等 | 排序        |        | 2020/8/20 | KW34/4 |     | KW0/6 |     | KW0/6 | 排序                       |
| KW6 | 周作业  | 493    | 翻转对               | 困难 | 排序        |        |           | KW0/6  |     | KW0/6 |     | KW0/6 | merge\-sort              |
| KW6 | 周作业  | 541    | 反转字符串 II          | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 151    | 翻转字符串里的单词         | 中等 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 557    | 反转字符串中的单词 III     | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 917    | 仅仅反转字母            | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 205    | 同构字符串             | 简单 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 680    | 验证回文字符串 Ⅱ         | 简单 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 300    | 最长上升子序列           | 中等 |           |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 91     | 解码方法              | 中等 |           |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 8      | 字符串转换整数 \(atoi\)  | 中等 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 1、直接写；2、正则表达式            |
| KW6 | 周作业  | 438    | 找到字符串中所有字母异位词     | 中等 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 5      | 最长回文子串            | 中等 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 32     | 最长有效括号            | 困难 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 818    | 赛车                | 困难 |           |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 44     | 通配符匹配             | 困难 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 周作业  | 115    | 不同的子序列            | 困难 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 709    | 转换成小写字母           | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 1、Ascii码；2、字典            |
| KW6 | 实战题目 | 58     | 最后一个单词的长度         | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 1、倒序计数（注意""和"a"）；2、split |
| KW6 | 实战题目 | 771    | 宝石与石头             | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 1、直接计数；2、哈希              |
| KW6 | 周作业  | 387    | 字符串中的第一个唯一字符      | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 1、暴力/count 2、哈希          |
| KW6 | 实战题目 | 14     | 最长公共前缀            | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 | 横向扫描                     |
| KW6 | 实战题目 | 344    | 反转字符串             | 简单 | 字符串       |        | 2020/8/22 | KW34/6 |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 242取消  | 有效的字母异位词          | 简单 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 49取消   | 字母异位词分组           | 中等 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 125    | 验证回文串             | 简单 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 72     | 编辑距离              | 困难 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 1143取消 | 最长公共子序列           | 中等 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
| KW6 | 实战题目 | 10     | 正则表达式匹配           | 困难 | 字符串       |        |           | KW0/6  |     | KW0/6 |     | KW0/6 |                          |
