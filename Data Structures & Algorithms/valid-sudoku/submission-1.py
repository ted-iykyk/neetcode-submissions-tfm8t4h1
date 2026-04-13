class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isSubGridValid(rowStart, rowEnd, colStart, colEnd):
            visited = set()

            for row in range(rowStart, rowEnd):
                for col in range(colStart, colEnd):

                    if board[row][col] in visited and board[row][col] != '.':
                        return False
                    visited.add(board[row][col])
            
            return True


        for rowBlock in range(3):
            for colBlock in range(3):
                if not isSubGridValid(rowBlock * 3, (rowBlock * 3) + 3, colBlock * 3, (colBlock * 3) + 3):
                    return False
        
        print('passed subGrid')
        # checking rows
        for row in range(len(board)):
            visited = set()
            for col in range(len(board[0])):
                if board[row][col] in visited and board[row][col] != '.':
                    return False
                visited.add(board[row][col])

        # checking cols 
        for col in range(len(board[0])):
            visited = set()
            for row in range(len(board)):
                if board[row][col] in visited and board[row][col] != '.':
                    return False
                visited.add(board[row][col])
        

        return True