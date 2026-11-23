class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #We use sets for O(1) lookup and duplicates
        # One hash for rows, one for col and one for squares

        
        cset = [set() for i in board]
        sqset = [set() for i in board]

        for i, row in enumerate(board):
            rset = set()

            for j, col in enumerate(row):
                
                # Validation for rows
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in rset:
                    rset.add(col)
                else:
                    return False

                # Validation for columns
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in cset[j]:
                    cset[j].add(col)
                else:
                    return False
                
                # Validate for Squares
                sq = (i // 3) * 3 + j // 3

                if board[i][j] == ".":
                    continue
                elif board[i][j] not in sqset[sq]:
                    sqset[sq].add(col)
                else:
                    return False
        return True

                
            