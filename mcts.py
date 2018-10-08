#!/usr/bin/env python3


"""
There's an off by one bug in the tree.number somewhere in here
"""


import random
import printing


ROLLOUT_FACTOR = 100
MCTS_FACTOR = 100


def do_mcts(tree):
    """
    Add Docstring

    """

    for _ in range(MCTS_FACTOR):

        mcts(tree)

def rollout(tree):
    """
    Add Docstring

    """

    for _ in range(ROLLOUT_FACTOR):

        rolled_game = tree.game[:]
        turn = tree.turn
        options = tree.options[:]

        while tree.calc_score(rolled_game) is None:

            choice = options.pop(random.randint(0, len(options)-1))

            if turn:

                rolled_game[choice] = True

            elif not turn:

                rolled_game[choice] = False

            turn = not turn

        tree.number += 1
        tree.wins += tree.calc_score(rolled_game)


def rollout_branches(tree):
    """
    Add Docstring

    """

    for branch in tree.branches:

        rollout(branch)


def backup(tree):
    """
    Add Docstring
    """

    while True:

        tree.number = 0
        tree.wins = 0

        for branch in tree.branches:

            tree.number += branch.number
            tree.wins += branch.wins
            branch.uct = branch.calc_uct()

        if tree.parent:

            tree = tree.parent

        else:

            return


def mcts(tree):
    """
    Add Docstring

    """




    leaf = find_leaf(tree)


    if leaf.calc_score() is not None:

        leaf.number += 1
        leaf.wins += 1

    else:

        leaf.make_branches()
        rollout_branches(leaf)
        backup(leaf)


def find_leaf(tree):
    """
    Add Docstring

    """

    #turn = tree.turn
    cur = tree

    while cur.branches != []:

        if cur.turn:

            highest = float('-inf')
            best = None

            for branch in cur.branches:

                if branch.uct > highest:

                    highest = branch.uct
                    best = branch

            cur = best

        elif not cur.turn:

            lowest = float('inf')
            best = None

            for branch in cur.branches:

                if branch.uct < lowest:

                    lowest = branch.uct
                    best = branch

            cur = best

    return cur


def find_best_move(tree):#move this to tree
    """
    Add Docstring

    """

    most_wins_ratio = float('-inf')
    best = None
    
    for branch in tree.branches:

        if branch.wins/branch.number > most_wins_ratio: #change to w/l, N...

            most_wins_ratio = branch.wins/branch.number
            best = branch

    return best
