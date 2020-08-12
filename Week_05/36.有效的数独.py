#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
# 1、一次迭代 96.55%/39.44%
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes= [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num  = board[i][j]
                if num != ".":
                    box_index= (i//3)*3 + j//3
                    rows[i][num] = rows[i].get(num,0) + 1
                    cols[j][num] = cols[j].get(num,0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num,0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True



# @lc code=end

