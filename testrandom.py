"""Example test you can run
to make sure your AI does better
than random."""
from isolation import Board
from test_players import RandomPlayer
from player_submission import CustomPlayer

if __name__ == "__main__":
    r = RandomPlayer()
    h = CustomPlayer()
    game = Board(h,r)
    game.play_isolation()