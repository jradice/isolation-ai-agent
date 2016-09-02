"""Example test you can run
to make sure your basic evaluation
function works."""
from isolation import Board
from test_players import RandomPlayer
from player_submission import OpenMoveEvalFn

if __name__ == "__main__":
    sample_board = Board(RandomPlayer(),RandomPlayer())
    # setting up the board as though we've been playing
    sample_board.move_count = 3
    sample_board.__active_player__ = 0 # player 1 = 0, player 2 = 1
    # 1st board = 7 moves
    sample_board.__board_state__ = [
                [0,2,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]
    ]
    sample_board.__last_player_move__ = {0: (2,2), 1: (0,1)}

    # player 1 should have 7 moves available,
    # so board gets a score of 7
    h = OpenMoveEvalFn()
    print('This board has a score of %s.'%(h.score(sample_board)))