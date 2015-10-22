#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Midterm"""

# game = [players[player::teams] for player in xrange(teams)]


def filter_list(players): # teams=3, min_team=1, max_team=None):
    """docstring"""
    newlist = [player for player in players if player[1] == 1 ]
            
    return newlist

    
def split_list(players):
    """docstring"""
    players = filter_list(players)
    listresult = []
    counter = 0
    listlen = len(players)
    for player in players:
        player = player[0]
        players[counter] = player
        counter += 1
    for player in players:
        listresult.append([item for item in player])
        listresult = [val for player in listresult for val in player]
        
    return listresult


def matchmaking(players, teams=3, min_team=1, max_team=None):
    players = split_list(players)
    accumulator = 0
    if max_team:
        listlen = max_team * teams
    else:
        listlen = len(players)
    game = [players[player:listlen:teams] for player in
                          xrange(teams)]
    accumulator += teams 
    if max_team * teams > len(players):
        game =  False
        
        
   # for player in xrange(teams):
        # game = [players[player::teams] for player in xrange(teams)]

    return game
    
    
PLIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1),
           ('g', 1), ('h', 0), ('i', 1), ('j', 0), ('k', 1), ('l', 1), ('m', 1),
         ('n', 1)]

print matchmaking(PLIST, teams=3, max_team=3)
