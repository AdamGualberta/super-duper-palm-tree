import string
from dank import *

class game(object):

   def __init__(self):
      
      self.currentBoard = gameboard()
      self.winState = True
      self.player1 = player("x")
      self.player2 = player("o")
      self.currentBoard.displayBoard()
      
   def play(self):
      while self.winState:
         self.currentBoard.updateBoard(self.player1.humanTurn(),
                                       self.player1)
         print(self.winState)
         if self.currentBoard.checkWinstate() == True:
            self.winState = False
            break
         else:
            self.currentBoard.updateBoard(self.player2.humanTurn(),
                                       self.player2)
            print(self.winState)
            if self.currentBoard.checkWinstate() == True:
               self.winState = False
               break
         
      return 0  