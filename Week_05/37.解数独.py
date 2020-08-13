#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution: #81.43%/5.57%
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1,10)) for _ in range(9)]
        col = [set(range(1,10)) for _ in range(9)]
        box = [set(range(1,10)) for _ in range(9)]
        empty=[] #收集需填数位置
        for i in range(9):
            for j in range(9):
                b = (i//3)*3+j//3
                if board[i][j] != ".":
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[b].remove(val)
                else:
                    empty.append((i,j))
        
        def backtrack(iter):
            if iter == len(empty):
                return True
            i,j = empty[iter]
            b = (i//3)*3+j//3
            for val in row[i] & col[j] & box[b]:
                row[i].remove(val)
                col[j].remove(val)
                box[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1): 
                    return True
                row[i].add(val)
                col[j].add(val)
                box[b].add(val)
            return False # 到这里肯定add过，所以就是没解出来
        backtrack(0)


# @lc code=end

