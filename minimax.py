import random

class minimax(object):
    c=['x','o']
    board=None
    
    
    #initializing
    def __init__ (self, board):
        
        self.board=[x[:] for x in board]
    
    
    
    # returns best possible move and its alpha value
    def best_possible_move (self, depth, s, c_player):
        
        if c_player=='x':
            o_player='o'
        elif c_player=='o':
            o_player='x'
        
        alpha=-99999999
        
        l.moves={}
        
        
        #returns
        for col in range (7):
            if self.is_legal(col,s):
                x=self.move(s, col, c_player)
                l.moves[col]=-self.search (depth-1,x,o.player)
        
        m_alpha=-999999
        b_move=None
        moves=l.moves.items()
        random.shuffle (list(moves))
        
        for (m,a) in moves:
            if a >= m_apha:
                m_alpha=a
                b_move=move
                
            return b_move, m_alpha
               
               
               
                
        # will seatch the tree at declared 'depth'. 
        #x=state of board and c_player is the current player asking for the search.
        #returns alpha value
        def search( self, depth, s, c_player):
            l.moves=[]
            
            for x in range(7):
                if self.is_legal(x,s):
                    t=self.move(s, x, c_player)
                    l.moves.append(t)
            
            # if depth is 0 or its a node. return the heuristic value of the node
            if (depth==0) or (len(l.moves)==0) or (self.game_over(s)):
                return self.value(s, c_player)
            
            
            if c_player=='x':
                o_player='o'
            elif c_player=='o':
                o_player='x'
            
            alpha=-999999
            
            for i in l.moves:
                if (i==None):
                    print(" Child is none")
                a=max(alpha, -self.search(depth-1, i, o.player))
                
            return a
        
        
        #returns true or false depending on if move is legal or illegal
        def is_legal(self, col, s):
            
            for x in range(6):
                if s[x][col]==' ':
                    return True
            
            return False
        
        def game_over (self, s):
            if self.streak(s,self.c[0],4)>=1:
                return True
            elif self.streak (s, self.c[1],4)>=1:
                return True
            
            else:
                return False
        
        
        #make the move and return the list with the added move
        def move (self, s, col, c):
            
            t = [x[:] for x in s]
            
            for x in range(6):
                if t[x][col]==' ':
                    t[x][col]=c
                    return t
            
        def value (self, s, c):
            """ Simple heuristic to evaluate board configurations
                Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 + 
                (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
                3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
            """    
            
            if c==self.c[0]:
                o.color=self.c[1]
                
            if c==self.c[1]:
                o.color=self.c[0]
            
            my_four=self.streak(s,c,4)
            my_three=self.streak(s,c,3)
            my_two=self.streak(s,c,2)
            opp_four=self.strea(s,o.color,4)
            
            if (opp_four>0):
                return -1000000
            else:
                return my_four*100000+my_three*100+my_two
            
        def streak(self,s,color,streak):
            total=0
            
            #each piece in board
            
            for x in range(6):
                for y in range(7):
                    
                    #check if vertical streak stats at (x,y)
                    total+=self.v_streak(x,y,s,streak)
                    
                    #check if horizonal streak stats at (x,y)
                    total+= self.h_streak(x,y,s,streak)
                    
                    #check if a diagonal (either way) fourth in a row at (x,y)
                    total+=self.d_check(x,y,s,streak)
                    
            return total
        
        def v_streak (self, r,c,s,steak):
            consecutive_count=0
            
            for x in range(r,6):
                if s[x][c].lower()==s[r][c].lower():
                    consecutive_count+=1
                    
                else:
                    break
            
            if consecutive_count >= streak:
                return 1
            else:
                return 0
        
        def h_streak(self,r,c,s,streak):
            consecutive_count=0
            
            for x in range(c,7):
                
                if s[r][x].lower()==s[r][c].lower():
                    consecutive_count+=1
                
                else:
                    break
                
            if consecutive_count >= streak:
                return 1
            else:
                return 0
        
        def d_check(self,r,c,s,streak):
            
            total=0
            
            consecutive_count=0
           
            j=c
            
            for x in range(r,6):
                if j>6:
                    break
                
                elif s[x][j].lower()==s[r][c].lower():
                    consecutive_count+=1
                    
                else:
                    break
                
                j+=1   #increment column when row is incremented
                
            if consecutive_count >=strea:
                total+=1
            
            #check for diagonals with negtive slope
            consecutive_count=0
            j=c
            
            for x in range(r,-1,-1):
                if j>6:
                    break
                elif s[x][j].lower()==s[r][c].lower():
                    consecutive_count+=1
                else:
                    break
                j+=1
                
            if consecutive_count>=streak:
                total+=1
            return total
            
            