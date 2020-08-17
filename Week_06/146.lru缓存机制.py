#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
# 1、利用OrderedDict 98.14%/74.8%
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.remain = capacity
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v =  self.dic.pop(key)
        self.dic[key] = v #作为dic最新元素
        return v
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)#必须要pop，直接赋值的话，后一个还存在
        else:
            if self.remain > 0:
                self.remain -=1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value
            

# 2、利用OrderedDict
# class LRUCache:

#     def __init__(self, capacity: int):


#     def get(self, key: int) -> int:


#     def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

