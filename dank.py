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
                #loops until it finds the height of the column
                if self.board[move][i] == ' ':
                    self.board[move][i] = player.getToken()#places player symbol on board
                    break
            self.displayBoard()
            
    def qUpdateBoard(self,move,player): #moves with no display shown
        #first check to see if the move will go out of bounds
        if self.validMove(move) == 0:
            #if not good it will display board again and prompt player to try again
            print("Move error")
        else:
            #moveNumber here for fun, doesn't do anything atm
            for i in range(0,6):
                #loops until it finds the height of the column
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
        #print(player.getToken())
        #print(player.getScore("h"))
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
        #print(player.getToken())
        #print(player.getScore("v"))
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
        #print(player.getToken())
        #print(player.getScore("d"))
        return False

    def validMove(self, move):
        #handles checking of out of bounds moves
        if len(self.board[move]) > 6:
            print("invalid move, column full")
            return 0
        else:
            return 1

    def checkWinstate(self, player):
        #uses check methods to see if the current board has a win state
        if self.hCheck(player) == True:
            #print(player.getType())
            #print("Winner by horizontal!")
            return True
        elif self.vCheck(player) == True:
            #print(player.getType())
            #print("Winner by vertical!")
            return True
        elif self.dCheck(player) == True:
            #print(player.getType())
            #print("Winner by diagonal!")
            return True
        else:
            return False
            
    def getBoard(self):
        return self.board

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
        self.heuristics = 0
        self.depth = 0
        self.diagonalScore = []
        self.horizontalScore = []
        self.verticalScore = []
        self.token = str(token)
        self.currentMove = ''
        self.type = type #human, monkey, dog, ai, etc.
        if self.type == "ai":
            self.difficulty = int(input("Difficulty 1-2: "))
            if self.difficulty == 2:
                self.depth = int(input("Depth for bot pls: "))
            #1 is random
            #2 TODO is minimax with low depth (or custom maybe)
            #3 TODO is minimax max depth infinite time and resources
        else:
            self.difficulty = 0 #redundant

    def Turn(self, gameboard, AI):
        #handles both human and ai turns depending on player type.
        if self.type == "ai":
            if self.difficulty == 1:
                self.currentMove = random.randint(1,7)
                return self.currentMove-1 #because index
            elif self.difficulty == 2:
                self.currentMove = AI.bestMove(self.depth, gameboard, self.playerNum)
                return self.currentMove-1
            elif self.difficulty == 3:
                #self.currentMove = minimax.nextMove()
                print("TODO: Implement minimax search")
            else:
                print("Wrong input.")
            
        else:
            #for the human player from stdin
            self.currentMove = int(input("Play a column...... "))
            return self.currentMove-1 #because index
            
    def setPlayerNum(self, number):
        self.playerNum = number

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
        elif direction == "all":
            temp = self.horizontalScore
            temp.extend(self.verticalScore)
            temp.extend(self.diagonalScore)
            return temp
   
    def getToken(self):
        #returns teh symbol that the player is using
        return self.token

    def getType(self):
        #yus
        return self.type
      
    def getDifficulty(self):
        return self.difficulty
        
    def setHeuristics(self, value):
        self.heuristics = value
        
    def getHeuristics(self):
        return self.heuristics
      
class minimax(object):

    def __init__(self, currBoard, currPlayer1, currPlayer2):
        self.board = currBoard #type gameboard
        self.players = [currPlayer1,currPlayer2]

    def search(self, depth, state, dank):
        #dank is player number
        """ Searches the tree at depth 'depth'
            By default, the state is the board, and dank is whomever 
            called this search
            
            Returns the alpha value
        """
        
        # enumerate all legal moves from this state
        player = self.players[dank]
        legal_moves = []
        for i in range(0,7):
            # if column i is a legal move...
            #print(i)
            if state.validMove(i):
                # make the move in column i for curr_player
                #temp = self.makeMove(state, i, curr_player)
                tempstate = state
                tempstate.qUpdateBoard(i,player)
                tempstate.checkWinstate(player)
                legal_moves.append(tempstate)
        
        # if this node (state) is a terminal node or depth == 0...
        if depth == 0 or len(legal_moves) == 0:
            # return the heuristic value of node
            #print("gg")
            return self.value(state, dank)
        
        # determine opponent's color

        alpha = -99999999
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
            if dank == 0:
                rank = 1
            else:
                rank = 0
            alpha = max(alpha, -self.search(depth-1, child, rank))
        return alpha
   
    def value(self, state, dank):
        #gets board heuristic data for current player
        """ Simple heuristic to evaluate board configurations
            Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 + 
            (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
            3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
        """
        if dank == 0:
            n = 0
            m = 1
        else:
            n = 1
            m = 0
        curr=self.players[n]
        opp=self.players[m]
        state.checkWinstate(curr)
        state.checkWinstate(opp)
        #print(self.players[n].getScore("all"))
        my_fours = self.players[n].getScore("all").count(3)
        my_threes = self.players[n].getScore("all").count(2)
        my_twos = self.players[n].getScore("all").count(1)
        opp_fours = self.players[m].getScore("all").count(3)
        #opp_threes = self.checkForStreak(state, o_color, 3)
        #opp_twos = self.checkForStreak(state, o_color, 2)
        if opp_fours > 0:
            return -100000
        else:
            return my_fours*100000 + my_threes*100 + my_twos
   
    def bestMove(self, depth, state, dank):
        """ Returns the best move (as a column number) and the associated alpha
            Calls search()
        """
        if dank == 0:
            rank = 1
        else:
            rank = 0
                
        # enumerate all legal moves
                
        self.player = self.players[dank]
        legal_moves = {} # will map legal move states to their alpha values
        for i in range(0,7):
            # if column i is a legal move...
            #print("  " + str(i))
            if state.validMove(i):
                # make the move in column i for curr_player
                #temp = self.makeMove(state, i, curr_player)
                temp = state
                temp.qUpdateBoard(i,self.player)
                legal_moves[i] = -self.search(depth-1, temp, rank)
        
        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        random.shuffle(list(moves))
        for move, alpha in moves:
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move
        
        #return best_move, best_alpha
        return best_move
   
   
   
   
   
   
   

