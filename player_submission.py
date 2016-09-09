#!/usr/bin/env python

# This file is your main submission that will be graded against. Only copy-paste
# code on the relevant classes included here from the IPython notebook. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.

# Submission Class 1
class OpenMoveEvalFn():
    """Evaluation function that outputs a 
    score equal to how many moves are open
    for your computer player on the board."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        return len(game.get_legal_moves())

# Submission Class 2
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        #if maximizing_player_turn:
        return len(game.get_legal_moves()) - len(game.get_opponent_moves())
        #return len(game.get_opponent_moves()) - len(game.get_legal_moves())

# Submission Class 3
class CustomPlayer():
    # TODO: finish this class!
    """Player that chooses a move using
    your evaluation function and
    a depth-limited minimax algorithm
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 1000 milliseconds."""
    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, legal_moves, time_left):

        #best_move, utility = self.minimax(game, depth=self.search_depth)
        # you will eventually replace minimax with alpha-beta
        best_move, utility = self.alphabeta(game, depth=self.search_depth)
        return best_move

    def utility(self, game, maximizing_player=True):
        """TODO: Update this function to calculate the utility of a game state"""

        if game.is_winner(self):
            return float("inf")

        if game.is_opponent_winner(self):
            return float("-inf")

        return self.eval_fn.score(game, maximizing_player)

    def minimax(self, game, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if self.terminal_test(game, depth):
            return None, self.utility(game)
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            if maximizing_player:
                results.append(self.min_value(game.forecast_move(action), depth - 1, not maximizing_player))
            else:
                results.append(self.max_value(game.forecast_move(action), depth - 1, not maximizing_player))
        best_val = max(results) if maximizing_player else min(results)
        best_index = results.index(best_val)
        best_move = actions[best_index]
        return best_move, best_val

    def max_value(self, game, depth, maximizing_player):
        if self.cutoff_test(game, depth):
            return self.utility(game, maximizing_player)
        v = float("-inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.min_value(game.forecast_move(action), depth - 1, not maximizing_player))
        if len(results) > 0:
            v = max(results)
        return v
    
    def min_value(self, game, depth, maximizing_player):
        if self.cutoff_test(game, depth):
            return self.utility(game, maximizing_player)
        v = float("inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.max_value(game.forecast_move(action), depth - 1, not maximizing_player))
        if len(results) > 0:
            v = min(results)
        return v

    def cutoff_test(self, game, depth):
        return depth == 0 or len(game.get_legal_moves()) == 0

    def alphabeta(self, game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if self.cutoff_test(game, depth):
            return None, self.utility(game)
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            if maximizing_player:
                results.append(self.min_value_AB(game.forecast_move(action), 
                                                 depth - 1, 
                                                 not maximizing_player,
                                                 alpha,
                                                 beta))
            else:
                results.append(self.max_value_AB(game.forecast_move(action), 
                                                 depth - 1, 
                                                 not maximizing_player,
                                                 alpha, 
                                                 beta))
        best_val = max(results) if maximizing_player else min(results)
        best_index = results.index(best_val)
        best_move = actions[best_index]
        return best_move, best_val
    
    def max_value_AB(self, game, depth, maximizing_player, alpha, beta):
        if self.cutoff_test(game, depth):
            return self.utility(game, maximizing_player)
        v = float("-inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.min_value_AB(game.forecast_move(action), 
                                             depth - 1, 
                                             not maximizing_player,
                                             alpha,
                                             beta))
            if len(results) > 0:
                v = max(results)
            if v >= beta:
                return v
            alpha = max([alpha, v])
        return v
    
    def min_value_AB(self, game, depth, maximizing_player, alpha, beta):
        if self.cutoff_test(game, depth):
            return self.utility(game, maximizing_player)
        v = float("inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.max_value_AB(game.forecast_move(action), 
                                             depth - 1, 
                                             not maximizing_player,
                                             alpha, 
                                             beta))
            if len(results) > 0:
                v = min(results)
            if v <= alpha:
                return v
            beta = min([beta, v])
        return v