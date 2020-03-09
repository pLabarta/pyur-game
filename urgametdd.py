from random import choice

def hello_world():
    return 'hello world'

def roll():
    last_roll = None
    last_score = 0
    last_roll = [choice(range(0,4,1)) for n in range(4)]
    last_score = sum([1 for each in last_roll if each % 2])
    return last_score

class Tile:
    
    def __init__(self):
        self.pieces = []
        self.war = False
        self.defence = False
        self.reroll = False

    def add_piece(self,piece):
        if len(self.pieces) == 0:
            self.pieces.append(piece)
            pass
        else:
            if self.war == True:
                if self.defence == True:
                    piece.owner.army.append(piece)
                else:
                    removed_piece = self.pieces.pop(0)
                    removed_piece.owner.army.append(removed_piece)
                    self.pieces.append(piece)
            else:
                self.pieces.append(piece)
    def set_war(self, state):
        self.war=state
    def set_defence(self,state):
        self.defence=state
    def set_reroll(self,state):
        self.reroll = state

class Piece:
    def __repr__(self):
        return f'{self.owner}'
    def __init__(self,player):
        self.owner = player
    # WOLOLO NOT IMPLEMENTED
    # def set_owner(self,owner):
    #     self.owner = owner
        # pass

class Player:
    def __init__(self,id):
        self.id = f'{id}'
        self.army = [Piece(self) for n in range(7)]
    def __repr__(self):
        return self.id
    def move(self,piece,tile):
        tile.add_piece(piece)
        self.army.pop(self.army.index(piece))
    army = []
    points = []

class Game:
    def new_game(self,players):
        self.board = [Tile() for n in range(14)]
        self.players = [Player(n) for n in range(players)]

class Board:
    def __init__(self):
        self.tiles = [Tile() for n in range(14)]
        self.tiles[3].set_reroll(True)
        self.tiles[7].set_reroll(True)
        self.tiles[7].set_defence(True)
        self.tiles[13].set_reroll(True)
        for each in self.tiles[4:12]:
            each.set_war(True)
    # def __repr__(self):
    #     return self.tiles


class Turns:
    players = [1,2,3,4]
    first = choice(players)
    def __init__(self):
        while self.players[0] != self.first:
            self.next_turn()
            print(f'{self.players}')
        print(f'juega {self.first}')
    def next_turn(self):
        alfondo = self.players[0]
        self.players.pop(0)
        self.players.append(alfondo)
        print(f'juega {self.players[0]}')

turns = Turns()