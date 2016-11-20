
import string
import random

class gameboard(object):
   """ 7 columns, 6 rows """
   def __init__(self):
      self.board = [[' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ']]
      self.moveNumber = 0
      self.rowCount = [0,0,0,0,0,0,0]
      """gameboard board is stored here in the form of a list of lists.
         the inner lists are teh columns.
         it goes board[column[row]] """

   def updateBoard(self,move,player):
      if self.validMove(move) == 0:
         self.displayBoard()
         self.updateBoard(player.Turn(),player)
      else:
         self.moveNumber += 1
         for i in range(0,6):
            if self.board[move][i] == ' ':
               self.board[move][i] = player.getToken()
               break
         self.displayBoard()
      """should pass a player object to this so that
         it can extract what token to use nicely!"""
   
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

   def hCheck(self):
   #it goes board[column[row]]
      for i in range(0,6):
         for j in range(0,4):
            hit = 0
            for k in range(1,4):
               if self.board[j][i] != ' ' and self.board[j+k][i] != ' ':
                  if self.board[j][i] == self.board[j+k][i]:
                     hit += 1
                     #print(hit)
                  if hit == 3:
                     return True
      return False

   def vCheck(self):
   #it goes board[column[row]]
      for i in range(0,7):
         for j in range(0,3):
            hit = 0
            for k in range(1,4):
               if self.board[i][j] != ' ' and self.board[i][j+k] != ' ':
                  if self.board[i][j] == self.board[i][j+k]:
                     hit += 1
                  if hit == 3:
                     return True
      return False

   def dCheck(self):
   #it goes board[column[row]]
      #left diagonal
      for i in range(0,3):
         for j in range(0,4):
            hit = 0
            for k in range(1,4):
               if self.board[j][i] != ' ' and self.board[j+k][i+k] != ' ':
                  if self.board[j][i] == self.board[j+k][i+k]:
                     hit += 1
                  if hit == 3:
                     return True
   #it goes board[column[row]]
       #right diagonal
      for i in range(0,3):
         for j in range(0,4):
            hit = 0
            for k in reversed(range(1,4)):
               if self.board[j+k][i] != ' ' and self.board[j][i+k] != ' ':
                  if self.board[j+k][i] == self.board[j][i+k]:
                     hit += 1
                  if hit == 3:
                     return True
      return False
      
   def validMove(self, move):
      if self.rowCount[move] > 5:
         print("invalid move, column full")
         return 0
      else:
         self.rowCount[move] += 1
         return 1

   def checkWinstate(self, player):
      if self.hCheck() == True:
         print(player.getType)
         print("Winner by horizontal!")
         return True
      elif self.vCheck() == True:
         print(player.getType)
         print("Winner by vertical!")
         return True
      elif self.dCheck() == True:
         print(player.getType)
         print("Winner by diagonal!")
         return True
      else:
         return False

   def printMove(self):
      print(self.moveNumber)

   def printRow(self, row):
      try:
         print("| " + self.board[0][row] + " | " + self.board[1][row]
         + " | " + self.board[2][row] + " | " + self.board[3][row]
         + " | " + self.board[4][row] + " | " + self.board[5][row]
         + " | " + self.board[6][row] + " |")
      except IndexError:
         print("Oh gosh, something went wrong with my index!")

   def printColumn(self, column):
      for i in range(0,7):
         try:
            print("| " + self.board[column][i] + " |")
         except IndexError:
            print("Oh gosh, something went wrong with my index!")
            
class player(object):

   def __init__(self, token, type):
      self.token = str(token)
      self.currentMove = ''
      self.type = type
      if self.type == "ai":
         self.difficulty = int(input("Difficulty 1-3: "))
      else:
         self.difficulty = 0

   def Turn(self):
      if self.type == "ai":
         if self.difficulty == 1:
            self.currentMove = random.randint(1,7)
            return self.currentMove-1 #because index
         elif self.difficulty == 2:
            print("TODO: Implement minimax search")
         elif self.difficulty == 3:
            print("TODO: Implement minimax search")
         else:
            print("Wrong input.")
            
      else:
         #for the human player from stdin
         self.currentMove = int(input("Play a column...... "))
         return self.currentMove-1 #because index
   
   def getToken(self):
      return self.token

   def getType(self):
      return self.type


















      