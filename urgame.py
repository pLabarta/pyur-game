from random import choice

def roll():
    last_roll = None
    last_score = 0
    last_roll = [choice(range(0,4,1)) for n in range(4)]
    last_score = sum([1 for each in last_roll if each % 2])
    return last_score

class Piece:
    player = None
    position = -1
    def __init__(self, player):
        self.player = player
    def set_player(self,player):
        self.player = player
        return self
    def set_position(self,position):
        self.position = position
    def __repr__(self):
        return f'{self.player} {self.position}'

class Tile:
    war = False
    defence = False
    reroll = False
    pieces = []
    def set_war(self, state):
        self.war = state
        return self
    def set_defence(self, state):
        self.defence = state
        return self
    def set_reroll(self, state):
        self.reroll = state
        return self
    def set_piece(self,piece):
        self.pieces += [piece]
        print(f'appendie una piece')
    def remove_piece(self,piece):
        self.pieces.remove(piece)
    def __repr__(self):
        return f'war: {self.war}, def: {self.defence}, rr: {self.reroll}, pieces: {self.pieces}'

class Rules:
    max_pieces = 7
    tiles = [Tile() for n in range(14)]
    tiles[3].set_reroll(True)
    tiles[7].set_reroll(True).set_defence(True)
    tiles[13].set_reroll(True)
    for each in tiles[4:12]:
        each.set_war(True)
    def get_tiles(self):
        return self.tiles
    def check_war(self, board, move):
        if board.tiles[move].war == True:
            True
        else:
            False
    def check_valid_move(self, board, move):
        if len(board.tiles[move].pieces) == 0 or (len(board.tiles[move].pieces) == 1 and 
        (board.tiles[move].pieces[0].player != board.current_player)):
            return True
        else:
            return False

class Board:
    rules = Rules()
    tiles = rules.get_tiles()
    players = []
    current_player = None
    def reset(self):
        self.tiles = [False for n in range(14)]
        return self
    def __repr__(self):
        return str([(self.tiles.index(tile)+1,tile) for tile in self.tiles])
    def next_player(self):
        for player in self.players:
            if player != self.current_player:
                return player
    def move(self,player,piece,steps):
        print(piece.position)
        print(steps)
        move = piece.position + steps
        print(move)
        if self.rules.check_valid_move(self, move):
            piece.position = move
            self.tiles[move].set_piece(piece)
            print(f'{player} creo una pieza en {move+1}')
        else:
            if self.rules.check_war(self, move):
                enemyPiece = self.tiles[move].pieces[0]
                enemyPiece.position = -1
                self.tiles[move].remove_piece(enemyPiece)
                self.tiles[move].set_piece(piece)
                print(f'{player} comio una pieza de {enemyPiece.player} en {move+1}')
            else:
                self.tiles[move].set_piece(piece)
                piece.position = move
                print(f'{player} movio una pieza a posicion {move+1}')
        
        if self.tiles[move].reroll == False:
            self.current_player = self.next_player()

    def new_game(self,players):
        for each in range(players):
            self.players.append(Player(f'Player{each}'))
        for player in self.players:
            player.pieces = [Piece(player) for n in range(self.rules.max_pieces)]
        if self.current_player == None:
            self.current_player = choice(self.players)
        print(f'{self.current_player} moves first')

    def play_turn(self):
        steps = roll()
        player = self.current_player
        self.move(player, player.get_free_piece(), steps)
    def play_turn_test(self, roll):
        player = self.current_player
        self.move(player, player.get_free_piece(), roll)


class Player:
    id = id
    pieces = []
    def __init__(self, id):
        self.id = id
    last_roll = 0
    def throw(self):
        self.last_roll = roll()
        return(self.last_roll)
    def get_free_piece(self):
        for piece in self.pieces:
            if piece.position == -1:
                print(f'haciendo falopa con {piece}, {len(self.pieces)}')
                return piece
    def __repr__(self):
        return f'{self.id}'
    # def get_moves(self):
    #     print(self.board)
    #     dice = self.last_roll
    #     if dice == 0:
    #         print('Tiraste 0 pete')
    #         return None
    #     else:
    #         # new piece option
    #         options = [n+1 for n in range(14) if self.board[dice] == False and n+1 == dice]
    #         # move piece options
    #         move_options = [n+1 for n in range(14) if self.board[n-dice] == True and self.board[n] == False]
    #         for each in move_options:
    #             options.append(each)
    #         print(options)
    #         return(options)

# board.get_moves(player)






# # Player Debug
# player = Player()
# print(player.pieces)
# print(player.board)
# print(player.last_roll)
# print('-rolling-')
# player.throw()
# print(player.last_roll)
# print('-getting moves-')
# player.get_moves()




    # def throw(self):
    #     dice = Dice()
    #     dice.throw()
    #     print(dice.last_roll)
    #     self.move = dice.last_roll
    # def move(self,position):
    #     if self.move != None:
    #         self.board[position] = True





board = Board()
board.new_game(2)
print(board)
board.play_turn_test(1)
print(board)



# print(board)
# board.play_turn_test(1)
# board.play_turn_test(2)
# board.play_turn_test(1)
# board.play_turn_test(3)
# print(board)
#print(board)
# print(board.move(player1,Ficha(),))




#         options = [player.board.index(n)+1 for n in player.board if player.board[n-player.move] or n+1-player.move == 0]
#         print(f'can move to {options}')

# game = Game()
# print(game.player1.move)
# game.throw(game.player1)
# print(game.player1.move)
# game.move(game.player1, 2)


