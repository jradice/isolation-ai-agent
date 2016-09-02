"""Example test to make sure
your minimax works, using the
#my_moves evaluation function."""
from isolation import Board
import isolation
from player_submission import CustomPlayer

if __name__ == "__main__":
    # create dummy 3x3 board
    p1 = CustomPlayer(search_depth=3)
    p2 = CustomPlayer()
    b = Board(p1,p2,3,3)
    b.__board_state__ = [
        [0,2,0],
        [0,0,1],
        [0,0,0]
    ]
    b.__last_player_move__[p1] = (1,2)
    b.__last_player_move__[p2] = (0,1)
    # use minimax to determine optimal move
    # sequence for player 1
    winner, move_history, termination = b.play_isolation()
    isolation.game_as_text(winner, move_history, termination)
    # your output should look like this:
    """
    ####################
      | 2 |   |
      |   | 1 |
      |   |   |

    ####################
    ####################
    1 | 2 |   |
      |   | - |
      |   |   |

    ####################
    ####################
    1 | - |   |
      |   | - |
      |   | 2 |

    ####################
    ####################
    - | - |   |
      |   | - |
      | 1 | 2 |

    ####################
    ####################
    - | - |   |
    2 |   | - |
      | 1 | - |

    ####################
    ####################
    - | - | 1 |
    2 |   | - |
      | - | - |

    ####################
    Illegal move at -1,-1.
    Player 1 wins.
    """