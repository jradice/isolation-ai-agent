"""Example test you can run
to make sure your AI does better
than random."""
from isolation import Board, game_as_text
from test_players import RandomPlayer
from player_submission import CustomPlayer

if __name__ == "__main__":
    r = RandomPlayer()
    h = CustomPlayer()
    game = Board(h,r)
    output = game.copy()
    winner, move_history, termination = game.play_isolation(time_limit=500)
    print game_as_text(winner, move_history, termination, output)