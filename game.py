from boardLayout import Board
import os

b=Board()
class Game():
      def __init__(self):
            self.board=b.board
            self.ROW=len(self.board)-1
            self.COL=len(self.board[0])-1
      
      def printBoard(self):
            b.boardLayout()

      def clearTerminal(self):
            os.system("cls")

      def movements(self, posX:int, posY:int, direction='W'):
            if self.board[posX][posY] == '*':
                  self.board[posX][posY]="*"
            else:
                  self.board[posX][posY]=self.board[posX][posY]
            if direction=='W':
                  posX-=1
                  if posX<0:
                        posX=self.ROW
                  return posX
            elif direction=='S':
                  posX+=1
                  if posX>self.ROW:
                        return 0
                  else:
                        return posX
            elif direction=='A':
                  posY-=1
                  if posY<0:
                        posY=self.COL
                  return posY
            elif direction=='D':
                  posY+=1
                  if posY>self.COL:
                        return 0
                  else:
                        return posY