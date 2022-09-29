"""Prints a good looking Terminal board"""
class Board():
      def __init__(self):
            self.board=[
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        ]

      def boardLayout(self): # This will print Board Layout
            border='-'
            HeadingCol='      | (1) | (2) | (3) | (4) | (5) | (6) | (7) | (8) | (9) |'
            print((str(border*55)).rjust(61))
            print(HeadingCol)
            for row in range(9):
                  print('|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|')
                  
                  print(f"| ({row+1})", end='')
                  for col in range(9):
                        print(" | ", self.board[row][col],end=' ')
                  print(' |')
            print(border*61)