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
        print("Welcome to the Connect 4 Alpha!")
        print("Difficulties are 1 and 2.")
        print("2 currently doesn't work, but is supposed to have minimax algorithm.")
        print("Please select 1 for difficulty for AI game.")
        type1 = str(input("Is player 1 'human' or 'ai'? "))
        type2 = str(input("Is player 2 'human' or 'ai'? "))
        self.player1 = player("x", type1)
        self.player1.setPlayerNum(0)
        self.player2 = player("o", type2)
        self.player2.setPlayerNum(1)
        #display the empty board, also good check to see if all is well.
        self.currentBoard.displayBoard()
      
    def play(self):
        #the main loop that keeps it all going
        #uses boolean while to loop, once false win state has been achieved.
        #basically a dank hack but it works nice and simple.
        
        while self.winState:
            self.currentBoard.updateBoard(self.player1.Turn(self.currentBoard, 0),
                                       self.player1)
            if self.currentBoard.checkWinstate(self.player1) == True:
                self.winState = False
                print("Player 1 wins!")
                break
            else:
                print(self.player2.getType())
                if self.player2.getDifficulty() == 2:
                    print("AI Battle")
                    tempBoard = self.currentBoard
                    m = minimax(self.player1, self.player2)
                    self.currentBoard.updateBoard(self.player2.Turn(tempBoard, m),
                                                                self.player2)
                else:
                    self.currentBoard.updateBoard(self.player2.Turn(self.currentBoard, 0),
                                                                self.player2)
                if self.currentBoard.checkWinstate(self.player2) == True:
                    self.winState = False
                    print("Player 2 wins!")
                    break
         
        return 0 #exit nicely