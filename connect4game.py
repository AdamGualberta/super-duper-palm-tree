#connect4 python implementation
#play stuff here
#Author = Adam Gendron, November 2016

import string
from dank import *

class game(object):
    
    def __init__(self):
        #initialize new gameboard
        self.currentBoard = gameboard()
        self.winState = True
        #setting players hardcoded, future maybe have as input
        self.player1 = player("x", "human")
        self.player2 = player("o", "bob")
        #display the empty board, also good check to see if all is well.
        self.currentBoard.displayBoard()
      
    def play(self):
        #the main loop that keeps it all going
        #uses boolean while to loop, once false win state has been achieved.
        #basically a dank hack but it works nice and simple.
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
         
        return 0 #exit nicely