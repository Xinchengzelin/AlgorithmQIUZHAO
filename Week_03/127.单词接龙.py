#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start

# 将问题抽象在一个无向无权图中，每个单词作为节点，差距只有一个字母的两个单词之间连一条边。
# 问题变成找到从起点到终点的最短路径
# 1、BFS
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    # def ladderLength(self, beginWord: str, endWord: str, wordList):
        if (not endWord in wordList) or (not beginWord) or (not endWord) or (not wordList):
            return 0
        L=len(wordList[0])
        all_combo_dict=defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" +word[i+1:]].append(word)
        queue=[(beginWord,1)]
        visited={beginWord:True}
        while queue:
            cur_word,level=queue.pop(0)
            for i in range(L):
                inter_word=cur_word[:i]+"*"+cur_word[i+1:]
                for word in all_combo_dict[inter_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word]=True
                        queue.append((word,level+1))
                all_combo_dict[inter_word]=[]
                # 如果之后还要再访问word就不可以了，避免了重复。但是BFS是同时多条路径的
                # 搜索，当前这条路径访问过了，记录下来，那如果其他路径需要再访问word呢？
                # 之后的路径再访问到next_word所需要的步数一定大于等于最先访问的这条路径。
                # 所以可以不再考虑。同理循环结束后，all_combo_dict[intermediate_word]
                # 中的所有单词都被访问过了，所以直接置空就好了，没必要再查看一次是否访问。
        return 0
        
        # print(all_combo_dict)
# Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
# @lc code=end

