#connect4 python implementation
#under the hood stuff here
#Author = Adam Gendron, November 2016

import string
import random

#gameboard: houses graphics, win state checks, current game progression
#player: houses player info, current move, move methods
#minimax: TODO will house minimax algorithm for ai player to use
#randomSearch: TODO put the random thing in its own class

class gameboard(object):
    #7 columns, 6 rows
    def __init__(self):
        self.board = [[' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ']]
        self.moveNumber = 0
        #rowCount keeps track of height of columns to keep in bounds
        self.rowCount = [0,0,0,0,0,0,0]
        """gameboard board is stored here in the form of a list of lists.
           the inner lists are teh columns.
           it goes board[column[row]] """

    def updateBoard(self,move,player):
        #first check to see if the move will go out of bounds
        if self.validMove(move) == 0:
            self.displayBoard()
            #if not good it will display board again and prompt player to try again
            self.updateBoard(player.Turn(),player)
        else:
            #moveNumber here for fun, doesn't do anything atm
            self.moveNumber += 1
            for i in range(0,6):
                #loops until it finds the height of the column TODO use rowCount here
                if self.board[move][i] == ' ':
                    self.board[move][i] = player.getToken()#places player symbol on board
                    break
            self.displayBoard()
   
    def displayBoard(self):
        for i in reversed(range(0,6)):
            try:
                print("| " + self.board[0][i] + " | " + self.board[1][i] \
                + " | " + self.board[2][i] + " | " + self.board[3][i] \
                + " | " + self.board[4][i] + " | " + self.board[5][i] \
                + " | " + self.board[6][i] + " |")
            except IndexError:
                print("Oh gosh, something went wrong with my index!")
        print("\n")
        
    #the following checks systematically check all possible win states. Not elegant but works.
        
    def hCheck(self, player):
        player.newScore("h", [])
        #it goes board[column][row]
        for i in range(0,6):
            hit = 0
            for j in range(0,6):
                if self.board[j][i] == player.getToken():
                    if self.board[j][i] == self.board[j+1][i]:
                        hit += 1
                    if hit == 3:
                        return True
                else:
                    if hit > 0:
                        player.setScore("h",hit)
                    hit = 0
            if hit > 0:
                player.setScore("h", hit)
        print(player.getToken())
        print(player.getScore("h"))
        return False
        
    def vCheck(self, player):
        player.newScore("v", [])
        #it goes board[column][row]
        for i in range(0,7):
            hit = 0
            for j in range(0,5):
                if self.board[i][j] == player.getToken():
                    if self.board[i][j] == self.board[i][j+1]:
                        hit += 1
                    if hit == 3:
                        return True
                else:
                    if hit > 0:
                        player.setScore("v",hit)
                    hit = 0
            if hit > 0:
                player.setScore("v", hit)
        print(player.getToken())
        print(player.getScore("v"))
        return False
        
    def dCheck(self, player):
        player.newScore("d", [])
        #it goes board[column][row]
        #neg slope
        for i in reversed(range(0,3)):
            for j in range(0,4):
                hit = 0
                for k in range(0,3):
                    if self.board[j+k][i+k] == player.getToken():
                        if self.board[j+k][i+k] == self.board[j+k+1][i+k+1]:
                            hit += 1
                        if hit == 3:
                            return True
                if hit > 0:
                    player.setScore("d",hit)
        #it goes board[column][row]
        #pos slope
        for i in reversed(range(3,6)):
            for j in reversed(range(0,4)):
                hit = 0 
                for k in range(0,3):
                    if self.board[j-k][i-k] == player.getToken():
                        if self.board[j-k][i-k] == self.board[j-k+1][i-k-1]:
                            hit += 1
                        if hit == 3:
                            return True
                if hit > 0:
                    player.setScore("d",hit)
        print(player.getToken())
        print(player.getScore("d"))
        return False

    #def hValue(self):
        
      
    def validMove(self, move):
        #handles checking of out of bounds moves
        if self.rowCount[move] > 5:
            print("invalid move, column full")
            return 0
        else:
            self.rowCount[move] += 1
            return 1

    def checkWinstate(self, player):
        #uses check methods to see if the current board has a win state
        if self.hCheck(player) == True:
            print(player.getType())
            print("Winner by horizontal!")
            return True
        elif self.vCheck(player) == True:
            print(player.getType())
            print("Winner by vertical!")
            return True
        elif self.dCheck(player) == True:
            print(player.getType())
            print("Winner by diagonal!")
            return True
        else:
            return False

    def printMove(self):
        #debug stuff
        print(self.moveNumber)

    def printRow(self, row):
        #debug stuff
        try:
            print("| " + self.board[0][row] + " | " + self.board[1][row]
            + " | " + self.board[2][row] + " | " + self.board[3][row]
            + " | " + self.board[4][row] + " | " + self.board[5][row]
            + " | " + self.board[6][row] + " |")
        except IndexError:
            print("Oh gosh, something went wrong with my index!")

    def printColumn(self, column):
        #debug stuff
        for i in range(0,7):
            try:
                print("| " + self.board[column][i] + " |")
            except IndexError:
                print("Oh gosh, something went wrong with my index!")
            
class player(object):

    def __init__(self, token, type):
        self.diagonalScore = []
        self.horizontalScore = []
        self.verticalScore = []
        self.token = str(token)
        self.currentMove = ''
        self.type = type #human, monkey, dog, ai, etc.
        if self.type == "ai":
            self.difficulty = int(input("Difficulty 1-3: "))
            #1 is random
            #2 TODO is minimax with low depth (or custom maybe)
            #3 TODO is minimax max depth infinite time and resources
        else:
            self.difficulty = 0 #redundant

    def Turn(self):
        #handles both human and ai turns depending on player type.
        if self.type == "ai":
            if self.difficulty == 1:
                self.currentMove = random.randint(1,7)
                return self.currentMove-1 #because index
            elif self.difficulty == 2:
                print("TODO: Implement minimax search")
            elif self.difficulty == 3:
                #self.currentMove = minimax.nextMove()
                print("TODO: Implement minimax search")
            else:
                print("Wrong input.")
            
        else:
            #for the human player from stdin
            self.currentMove = int(input("Play a column...... "))
            return self.currentMove-1 #because index
            
    def newScore(self, direction, scorelist):
        if direction == "h":
            self.horizontalScore = scorelist
        elif direction == "v":
            self.verticalScore = scorelist
        elif direction == "d":
            self.diagonalScore = scorelist
   
    def setScore(self, direction, score):
        if direction == "h":
            self.horizontalScore.append(score)
        elif direction == "v":
            self.verticalScore.append(score)
        elif direction == "d":
            self.diagonalScore.append(score)
            
    def getScore(self, direction):
        if direction == "h":
            return self.horizontalScore
        elif direction == "v":
            return self.verticalScore
        elif direction == "d":
            return self.diagonalScore
   
    def getToken(self):
        #returns teh symbol that the player is using
        return self.token

    def getType(self):
        #yus
        return self.type
      
    def getDifficulty(self):
        return self.difficulty
      
class ai():

    def randomMove(self):
        return random.randint(1,7)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   

