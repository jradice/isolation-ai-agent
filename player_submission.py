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
        return len(game.get_legal_moves()) - len(game.get_opponent_moves())

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
    def __init__(self, search_depth=3, eval_fn=CustomEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth
        self.opening_moves = [(3,3), (0,3), (3,6), (6,3), (3,0)]

    def move(self, game, legal_moves, time_left):
        if len(legal_moves) == 1:
            return legal_moves[0]
        if game.move_count < 2:
            for move in self.opening_moves:
                if game.move_is_legal(move[0], move[1]):
                    return move
        else:
            # Attempt to reflect opponents move
            #if game.move_count >= 4:
            #   best_move = self.get_reflected_move(game, legal_moves)
            #   if game.move_is_legal(best_move[0], best_move[1]):
            #        return best_move
                
            #best_move, utility = self.minimax(game, depth=self.search_depth)
            #return best_move
            # you will eventually replace minimax with alpha-beta

            # Alpha-beta pruning
            #best_move, utility = self.alphabeta(game, depth=self.search_depth)
            #return best_move

            # Iterative Deepening
            self.search_depth = len(game.get_blank_spaces())
            best_moves = {}
            id_level = 1
            #print "Move %d ####################" % game.move_count
            #print "Search Depth: %d" % self.search_depth
            while time_left() > 250 and id_level <= self.search_depth:
                #print "Time left:  %d" % time_left()
                #print "Iterative Deepening Level: %d" % id_level
                # Alpha-beta pruning
                best_move, utility = self.alphabeta(game, time_left, depth=self.search_depth)
                #print "Time left:  %d" % time_left()
                best_moves[utility] = best_move
                id_level += 1
            #print "Eval Result: %f" % max(best_moves.keys(), key=float)
            #print "############################"
            best_move = best_moves[max(best_moves.keys(), key=float)]
            return best_move

    def utility(self, game, maximizing_player=True):
        """TODO: Update this function to calculate the utility of a game state"""

        if game.is_winner(self):
            return float("inf")

        if game.is_opponent_winner(self):
            return float("-inf")

        return self.eval_fn.score(game, maximizing_player)

    def minimax(self, game, time_left, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if self.cutoff_test(game, time_left, depth):
            return None, self.utility(game)
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            if maximizing_player:
                results.append(self.min_value(game.forecast_move(action), time_left, depth - 1, not maximizing_player))
            else:
                results.append(self.max_value(game.forecast_move(action), time_left, depth - 1, not maximizing_player))
        best_val = max(results) if maximizing_player else min(results)
        best_index = results.index(best_val)
        best_move = actions[best_index]
        return best_move, best_val

    def max_value(self, game, time_left, depth, maximizing_player):
        if self.cutoff_test(game, time_left, depth):
            return self.utility(game, maximizing_player)
        v = float("-inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.min_value(game.forecast_move(action), time_left, depth - 1, not maximizing_player))
        if len(results) > 0:
            v = max(results)
        return v
    
    def min_value(self, game, time_left, depth, maximizing_player):
        if self.cutoff_test(game, time_left, depth):
            return self.utility(game, maximizing_player)
        v = float("inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.max_value(game.forecast_move(action), time_left, depth - 1, not maximizing_player))
        if len(results) > 0:
            v = min(results)
        return v

    def cutoff_test(self, game, time_left, depth):
        #print "CUTOFF: Depth: %d" % depth
        #print "CUTOFF: Time left: %d" % time_left()
        return depth == 0 or len(game.get_legal_moves()) == 0 or time_left() < 60

    def alphabeta(self, game, time_left, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if self.cutoff_test(game, time_left, depth):
            return None, self.utility(game)
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            if maximizing_player:
                results.append(self.min_value_AB(game.forecast_move(action),
                                                 time_left,
                                                 depth - 1, 
                                                 not maximizing_player,
                                                 alpha,
                                                 beta))
            else:
                results.append(self.max_value_AB(game.forecast_move(action), 
                                                 time_left,
                                                 depth - 1, 
                                                 not maximizing_player,
                                                 alpha, 
                                                 beta))
        best_val = max(results) if maximizing_player else min(results)
        best_index = results.index(best_val)
        best_move = actions[best_index]
        return best_move, best_val
    
    def max_value_AB(self, game, time_left, depth, maximizing_player, alpha, beta):
        if self.cutoff_test(game, time_left, depth):
            return self.utility(game, maximizing_player)
        v = float("-inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.min_value_AB(game.forecast_move(action), 
                                             time_left,
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
    
    def min_value_AB(self, game, time_left, depth, maximizing_player, alpha, beta):
        if self.cutoff_test(game, time_left, depth):
            return self.utility(game, maximizing_player)
        v = float("inf")
        results = []
        actions = game.get_legal_moves()
        for action in actions:
            results.append(self.max_value_AB(game.forecast_move(action), 
                                             time_left,
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

    def get_reflected_move(self, game, legal_moves):
        opponent = game.get_inactive_player()
        opponent_locations = game.get_player_locations(opponent)
        opponent_quadrant = self.get_quadrant(opponent_locations[len(opponent_locations) - 2],
                                         opponent_locations[len(opponent_locations) - 1])
        last_location = game.get_last_move_for_player(self)
        reflected_moves = {}
        for move in legal_moves:
            utility = float("-inf")
            quadrant = self.get_quadrant(last_location, move)
            if opponent_quadrant == 0 and quadrant == 2:
                utility = self.eval_fn.score(game.forecast_move(move))
                reflected_moves[utility] = move
            if opponent_quadrant == 1 and quadrant == 3:
                utility = self.eval_fn.score(game.forecast_move(move))
                reflected_moves[utility] = move
            if opponent_quadrant == 2 and quadrant == 0:
                utility = self.eval_fn.score(game.forecast_move(move))
                reflected_moves[utility] = move
            if opponent_quadrant == 3 and quadrant == 1:
                utility = self.eval_fn.score(game.forecast_move(move))
                reflected_moves[utility] = move
        if len(reflected_moves.keys()) == 0:
            return (-1, -1)
        return reflected_moves[max(reflected_moves.keys(), key=float)]

    def get_quadrant(self, a, b):
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        if dx < 0 and dy < 0:
            return 0
        if dx < 0 and dy > 0:
            return 1
        if dx > 0 and dy > 0:
            return 2
        if dx < 0 and dy > 0:
            return 3