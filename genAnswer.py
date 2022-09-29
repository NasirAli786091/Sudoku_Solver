from game import Game

"""This will generate the desired answer if possible"""
game=Game()
class AnswerGenerator():

      def isValid(self, board:list[list[str]], row:int, col:int, val:str):
            for r in range(9):
                  if board[r][col]==str(val):
                        return False
            for c in range(9):
                  if board[row][c]==str(val):
                        return False

            rowStart=(row//3)*3
            colStart=(col//3)*3
            for r in range(rowStart, rowStart+3):
                  for c in range(colStart, colStart+3):
                        if board[r][c]==str(val):
                              return False

            return True

      def sudokuSolver(self, board:list[list[str]], r:int, c:int):
            if r==9:
                  game.printBoard()
                  # print(board)
                  # timeEnd=time()
                  # print(timeEnd-timeStart)
                  return
            if c==8:
                  nextR=r+1
                  nextC=0
            else:
                  nextR=r
                  nextC=c+1
            if board[r][c]!=' ':
                  self.sudokuSolver(board, nextR, nextC)
            else:
                  for val in range(1, 10):
                        if self.isValid(board, r, c, val):
                              board[r][c]=str(val)
                              self.sudokuSolver(board, nextR, nextC)
                              board[r][c]=' '