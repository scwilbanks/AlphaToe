#!/usr/bin/env python3

"""
Add Docstring

"""


import math


NEW_GAME = [None] * 9


class Tree():
    """
    Add Docstring

    """


    def __init__(self, game, xoro, turn, root=False):
        """
        Add Docstring
        Too many instance attributes (13/7)
        """

        self.xoro = xoro
        self.opponent = not xoro #take out
        self.turn = turn
        self.game = game
        self.number = 0
        self.wins = 0
        self.root = root
        self.parent = None
        self.uct = None
        self.constant = 1 #take out
        self.best = None #take out

        self.options = self.make_options()

        self.branches = []


    def make_options(self):
        """
        Add Docstring

        """

        options = []

        for i in range(len(self.game)):
            if self.game[i] is None:
                options.append(i)

        return options


    def make_branches(self):
        """
        Add Docstring

        """

        branches = []

        if self.options == []:
            return None

        for option in self.options:
            game = self.game[:]
            game[option] = self.turn
            branch = Tree(game, self.xoro, not self.turn)
            branch.parent = self
            branches.append(branch)

        self.branches = branches

        return branches

    def calc_uct(self):
        """
        Add Docstring

        """
        wins = self.wins
        number = self.number
        constant = self.constant
        parent_number = self.parent.number

        return (wins/number) + constant*pow(math.log(parent_number)/number, .5)


    def calc_score(self, game=None):
        """
        Add Docstring

        """

        if not game:
            game = self.game

        wins = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
            ]

        result = None

        for win in wins:
            if game[win[0]] is not None:
                if game[win[0]] == game[win[1]] == game[win[2]]:
                    if game[win[0]] == self.xoro:
                        result = 1
                    else:
                        result = -1

        if result is None and None not in game:
            result = 0

        return result
