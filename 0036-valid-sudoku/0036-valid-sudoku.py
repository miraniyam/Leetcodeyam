class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0, 9):
            # row
            row_list = [x for x in board[i] if x != "."]
            row_set = set(row_list)
            if len(row_list) != len(row_set):
                return False
            
            # col
            col_list = [board[j][i] for j in range(0, 9) if board[j][i] != "."]
            col_set = set(col_list)
            if len(col_list) != len(col_set):
                return False

            # subbox
                # pattern
                # i : 0,1,2 -> 0
                #     3,4,5 -> 3
                #     6,7,8 -> 6
                # j : 0,3,6 -> 0
                #     1,4,7 -> 3
                #     2,5,8 -> 6
            subbox_list = [
                board[(i//3)*3][3*(i%3)], board[(i//3)*3][3*(i%3)+1], board[(i//3)*3][3*(i%3)+2],
                board[(i//3)*3+1][3*(i%3)], board[(i//3)*3+1][3*(i%3)+1], board[(i//3)*3+1][3*(i%3)+2],
                board[(i//3)*3+2][3*(i%3)], board[(i//3)*3+2][3*(i%3)+1], board[(i//3)*3+2][3*(i%3)+2]
            ]
            
            subbox_list = [x for x in subbox_list if x != "."]
            subbox_set = set(subbox_list)
            if len(subbox_list) != len(subbox_set):
                return False

        return True

                
        