import unittest
from urgametdd import *


# Todo lo que se testea con el mismo setup va junto en una clase

class TestFunctions(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    def test_roll_should_return_0123or4(self):
        self.assertIn(roll(),[0,1,2,3,4])

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    def test_game_creates_players(self):
        self.game.new_game(2)
        for each in self.game.players:
            self.assertIsInstance(each, Player)

class TestTile(unittest.TestCase):
    piece = Piece(Player('test_player'))
    other_player_piece = Piece(Player('other_test_player'))

    def setUp(self):
        self.tile = Tile()
        

    def test_war(self):
        self.tile.set_war(True)
        self.assertEqual(self.tile.war, True)

    def test_not_war(self):
        self.tile.set_war(False)
        self.assertEqual(self.tile.war, False)

    def test_defence(self):
        self.tile.set_defence(True)
        self.assertEqual(self.tile.defence, True)
        
    def test_not_defence(self):
        self.tile.set_defence(False)
        self.assertEqual(self.tile.defence, False)

    def test_reroll(self):
        self.tile.set_reroll(True)
        self.assertEqual(self.tile.reroll, True)

    def test_not_reroll(self):
        self.tile.set_reroll(False)
        self.assertEqual(self.tile.reroll, False)

    def test_add_piece(self):
        self.tile.add_piece(self.piece)
        self.assertIn(self.piece,self.tile.pieces)

    def test_pieces_share_not_war_tiles(self):
        self.tile.set_war(False)
        self.tile.add_piece(self.other_player_piece)
        self.tile.add_piece(self.piece)
        self.assertIn(self.piece, self.tile.pieces)
        self.assertIn(self.other_player_piece, self.tile.pieces)

    def test_add_pieces_at_war_tiles(self):
        self.tile.set_war(True)
        self.tile.add_piece(self.other_player_piece)
        self.tile.add_piece(self.piece)
        self.assertIn(self.piece, self.tile.pieces)
        self.assertNotIn(self.other_player_piece, self.tile.pieces)

    def test_add_pieces_at_war_and_defended_tiles(self):
        self.tile.set_war(True)
        self.tile.set_defence(True)
        self.tile.add_piece(self.other_player_piece)
        self.tile.add_piece(self.piece)
        self.assertNotIn(self.piece, self.tile.pieces)
        self.assertIn(self.other_player_piece, self.tile.pieces)
        
class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece(Player('test_player'))
    # WOLOLO NOT IMPLEMENTED
    # def test_set_owner(self):
    #     self.piece.set_owner('Jugador')
    #     self.assertEqual(self.piece.owner, 'Jugador')

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('test_player')
        self.other_player = Player('other_test_player')
        self.tile = Tile()
    
    def test_player_starts_with_seven_pieces(self):
        self.assertTrue(len(self.player.army) == 7)

    def test_if_player_places_in_free_tile_loses_army(self):
        piece = self.player.army[0]
        self.player.move(piece, self.tile)
        self.assertIn(piece, self.tile.pieces)
        self.assertNotIn(piece, self.player.army)

    def test_pieces_generated_are_owned_by_player(self):
        piece = self.player.army[0]
        self.assertEqual(piece.owner, self.player)

    def test_player_places_in_war_tile_with_enemy_piece(self):
        # given
        piece = self.player.army[0]
        other_piece = self.other_player.army[0]
        self.tile.set_war(True)
        self.other_player.move(other_piece,self.tile)
        # when
        self.player.move(piece,self.tile)
        # then
        self.assertNotIn(other_piece,self.tile.pieces)
        self.assertIn(other_piece,self.other_player.army)
        self.assertIn(piece,self.tile.pieces)
        self.assertNotIn(piece, self.player.army)
    def test_player_places_in_defended_war_tile_with_enemy_piece(self):
        # given
        piece = self.player.army[0]
        other_piece = self.other_player.army[0]
        self.tile.set_war(True)
        self.tile.set_defence(True)
        self.other_player.move(other_piece,self.tile)
        # when
        self.player.move(piece, self.tile)
        # then
        self.assertIn(other_piece,self.tile.pieces)
        self.assertNotIn(other_piece,self.other_player.army)
        self.assertNotIn(piece,self.tile.pieces)
        self.assertIn(piece, self.player.army)

class TestMove:
    def setUp(self):
        self.player = Player('test_player')
        self.other_player = Player('other_test_player')
        self.tile = Tile()

    # Convertir player.move en una clase independiente

    # Assert pieces assert in tile/player transformar en un metodo

    # Board se genere con default o con posibilidad de modificarlo

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    def test_board_has_tiles(self):
        for each in self.board.tiles:
            self.assertIsInstance(each, Tile)
    def test_board_tiles_meet_standard_rules(self):
        # then
        # reroll
        self.assertTrue(self.board.tiles[3].reroll)
        self.assertTrue(self.board.tiles[7].reroll)
        self.assertTrue(self.board.tiles[13].reroll)
        # war
        for each in range(4,12):
            print(each)
            self.assertTrue(self.board.tiles[each].war)
        # defence
        self.assertTrue(self.board.tiles[7].defence)


if __name__ == '__main__':
    unittest.main()
