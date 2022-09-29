from game import Game
from genAnswer import AnswerGenerator

MOVEMENTS=['w', 'a', 's', 'd', 'W', 'A', 'S', 'D']
VALUES=['1', '2', '3', '4', '5', '6', '7', '8', '9']

game=Game()
genAns=AnswerGenerator()

# a initial position in board of "*"
positionX=4
positionY=4

# MAIN PROGRAMS
while True:
      game.clearTerminal() #To clean the Terminal

      print('|-|-|  COMMANDS  |-|-|')
      print('       W -> Upward \n       S -> Downward\n       A -> Left\n       D -> Right')
      print("       O -> Delete\n       Y -> Generate Answer")

      if game.board[positionX][positionY] !='*':
            boardVal=game.board[positionX][positionY]

      lastPosX, lastPosY=positionX, positionY
      game.board[positionX][positionY]='*'
      game.printBoard()


      """A inside while loop to get the desired input from the Player"""
      while True:
            userInput=input('cmd ---> ').upper()
            if userInput in MOVEMENTS or userInput in VALUES or userInput=='O' or userInput=="Y":
                  break
            else:
                  print('Either move the "*" or choose a number in range 1-9 including')

      
      if userInput in MOVEMENTS:
            if userInput=='W' or userInput=='S':
                  positionX=game.movements(positionX, positionY, userInput)
                  game.board[lastPosX][lastPosY]=boardVal
            else:
                  positionY=game.movements(positionX, positionY, userInput)
                  game.board[lastPosX][lastPosY]=boardVal
      elif userInput in VALUES:
            game.board[positionX][positionY]=userInput


      if userInput.upper()=='O': #delete the current Index value
            game.board[positionX][positionY]=' '

      if userInput.upper()=='Y': # generate Answer
            if game.board[positionX][positionY] == '*':
                  game.board[positionX][positionY]=' '
            genAns.sudokuSolver(game.board, 0, 0)
            
            break #This will end the program ones the user input is 'Y'