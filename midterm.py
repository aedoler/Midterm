#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Midterm"""


def filter_list(players):
    """Filters out bad connections of players (tuples containing 0
       instead of 1.
       Arguments:
           players (list): List containing tuples with player name and a 1 or 0
       Returns:
           A list of tuples (players) without those containing 0s
       Examples:
           LIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1)]
           filter_list(LIST)
           >>>[('a', 1), ('b', 1), ('d', 1), ('f', 1)]
    """
    newlist = [player for player in players if player[1] == 1]

    return newlist


def split_list(players):
    """Removes parenthesis and int "1" to output a clean list of players.
       Arguments:
           players (list): List containing tuples of player name and int 1
       Returns:
           list of players in a single list, non-nested
       Examples:
           LIST = [('a', 1), ('b', 1), ('d', 1), ('f', 1)]
           split_list(LIST)
           >>>[a, b, d, f]
    """
    players = filter_list(players)
    listresult = []
    counter = 0
    for player in players:
        player = player[0]
        players[counter] = player
        counter += 1
    for player in players:
        listresult.append([item for item in player])
        listresult = [val for player in listresult for val in player]
        # Last line cleans up extra brackets from list

    return listresult


def matchmaking(players, teams=3, min_team=1, max_team=None):
    """ Sorts players into even teams based on input, in round-robin selection.
    Arguments:
        players (list): list of players to be sorted into teams
        teams (int): default=3, amount of teams, determines round-robin count
        min_team (int): minimum number of players per team
        max_team (int): maximum number of players per team
    Returns:
        List of teams represented as nested lists, based on argument input
        If not enough players to return input, returns 'False'
    Examples:
        LIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1),
        ('g', 1), ('h', 0), ('i', 1), ('j', 0), ('k', 1), ('l', 1), ('m', 1),
        ('n', 1), ('o', 1), ('p', 1)]
        matchmaking(LIST, teams=4, max_team=3)
        >>>[['a', 'g', 'm'], ['b', 'i', 'n'], ['d', 'k', 'o'], ['f', 'l', 'p']]
        matchmaking(LIST, teams=6, max_teams=4)
        >>>False
        matchmaking(LIST, teams=2, min_team=4)
        >>>[['a', 'd', 'g', 'k', 'm', 'o'], ['b', 'f', 'i', 'l', 'n', 'p']]
    """
    players = split_list(players)
    if max_team:
        listlen = max_team * teams
        game = [players[player:listlen:teams] for player in
                xrange(teams)]
    else:
        listlen = len(players)
        if min_team:
            game = [players[player:listlen:teams] for player in
                    xrange(teams)]
    if max_team:
        if max_team * teams > len(players):
            if min_team * teams < len(players):
                listlen = len(players)
            elif min_team * teams > len(players):
                game = False
    elif not max_team:
        if min_team:
            if min_team * teams > len(players):
                game = False

    return game


PLIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1),
         ('g', 1), ('h', 0), ('i', 1), ('j', 0), ('k', 1), ('l', 1), ('m', 1),
         ('n', 1), ('o', 1), ('p', 1)]

print matchmaking(PLIST, teams=3, min_team=2, max_team=9)
