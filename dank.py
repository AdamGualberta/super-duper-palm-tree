
import string

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
      """gameboard board is stored here in the form of a list of lists.
         the inner lists are teh columns.
         it goes board[column[row]] """

   def updateBoard(self,move,player):
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

   def checkWinstate(self):
      if self.hCheck() == True:
         print("Winner")
         return True
      elif self.vCheck() == True:
         print("Winner")
         return True
      elif self.dCheck() == True:
         print("Winner")
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

   def __init__(self, token):
      self.token = str(token)
      self.currentMove = ''

   def humanTurn(self):
      self.currentMove = int(input("Play a column...... "))
      return self.currentMove-1 #because index
   
   def getToken(self):
      return self.token




















      