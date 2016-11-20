import string
from dank import *

class game(object):

   def __init__(self):
      
      self.currentBoard = gameboard()
      self.winState = True
      self.player1 = player("x", "human")
      self.player2 = player("o", "ai")
      self.currentBoard.displayBoard()
      
   def play(self):
      while self.winState:
         self.currentBoard.updateBoard(self.player1.Turn(),
                                       self.player1)
         if self.currentBoard.checkWinstate(self.player1) == True:
            self.winState = False
            break
         else:
            self.currentBoard.updateBoard(self.player2.Turn(),
                                       self.player2)
            if self.currentBoard.checkWinstate(self.player2) == True:
               self.winState = False
               break
         
      return 0