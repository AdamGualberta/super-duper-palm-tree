import random

class MinimaxCustom(self):

    def __init__(self, baord):
        #idk
    def bestMove(depth, player):

        if player == 'x':
            opp_player = 'o'
        else:
            opp_player = 'x'

        poss_moves = {}
        for i in range(7):
            if self.isLegalMove(i):
                var = self.makeMove(i, player)

        alpha = -999999
        ayy_move = None
        moves = legal_moves.items()
        random.shuffle(list(moves))
        for move, a in moves:
            if a >= alpha:
                alpha = a
                ayy_move = move


            
