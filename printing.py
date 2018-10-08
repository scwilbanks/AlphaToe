#!/usr/bin/env python3


"""
Provides functions to print games and tree nodes.

"""


def print_properties(node):
    """
    Add Docstring

    """

    print("N =", node.number)
    print("W =", node.wins)
    print("UCT =", node.uct)


def print_game(game):
    """
    Add Docstring

    """

    game_string = ''
    for square in game:
        if square is True:
            game_string += 'X'
        elif square is False:
            game_string += 'O'
        elif square is None:
            game_string += ' '

    line = '-' * 7

    print(line)
    print('|'+game_string[0]+'|'+game_string[1]+'|'+game_string[2]+'|')
    print(line)
    print('|'+game_string[3]+'|'+game_string[4]+'|'+game_string[5]+'|')
    print(line)
    print('|'+game_string[6]+'|'+game_string[7]+'|'+game_string[8]+'|')
    print(line)


def print_node(node):
    """
    Add Docstring

    """

    print('---------------')
    if node.turn:
        print("X's turn:")
    else:
        print("O's turn:")
    print_game(node.game)
    print_properties(node)

def print_tree(tree):
    """
    Add Docstring

    """

    print("current tree:")
    print_node(tree)
    for branch in tree.branches:
        print()
        print_tree(branch)
