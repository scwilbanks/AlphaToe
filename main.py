#!/usr/bin/env python3


"""
Main game loop.

"""


import tree
import printing
import mcts


NEW_GAME = [None] * 9


def my_turn(cur):
    """
    This function executes the player's turn and returns the next game state.

    Args:
        cur: node of class Tree of current game.

    Retuns:
        Returns node of game that corresponds with the move made this turn.

    """
    
    printing.print_game(cur.game)

    mcts.do_mcts(cur)

    best = mcts.find_best_move(cur)
    print('best move')
    printing.print_node(best)

    moving = True
    while moving:
        my_move = int(input("My move >"))
        if cur.game[my_move-1] is None:
            moving = False

    current_game = cur.game
    current_game[my_move-1] = cur.turn

    for branch in cur.branches:
        if branch.game == current_game:
            cur = branch
            break

    if cur.calc_score() is not None:
        quit()

    return cur


def opponent_turn(cur):
    """
    This function executes the opponents turn and returns the next game state.

    Args:
        cur: node of class Tree of current game.

    Retuns:
        Returns node of game that corresponds with the move made this turn.

    """

    printing.print_game(cur.game)

    mcts.do_mcts(cur)

    moving = True
    while moving:
        opponent_move = int(input("Opponent's move >"))
        if cur.game[opponent_move-1] is None:
            moving = False

    current_game = cur.game
    current_game[opponent_move-1] = cur.turn

    for branch in cur.branches:
        if branch.game == current_game:
            cur = branch
            break

    if cur.calc_score() is not None:
        quit()

    return cur



def play():

    """
    Executes the game.

    Args:
        None

    Returns:
        None

    """

    print('Play as X or O?')
    x_or_o = input('>')

    if x_or_o == 'x':
        playing_x = True
    elif x_or_o == 'o':
        playing_x = False

    cur = None
    turn = True

    print("New Game")

    while True:

        if not cur:
            if playing_x:
                cur = tree.Tree(NEW_GAME, playing_x, turn)
            if not playing_x:
                printing.print_game(NEW_GAME)
                opponent_move = int(input("Opponent's move >"))
                game = NEW_GAME
                game[opponent_move-1] = True
                cur = tree.Tree(game, playing_x, not turn)

        cur = my_turn(cur)
        cur = opponent_turn(cur)

play()
