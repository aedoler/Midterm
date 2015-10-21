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
        
    return listresult

def matchmaking(players, teams=3, min_team=1, max_team=None):
    players = split_list(players)
    listresult = []
    for player in xrange(teams):
        game = [players[player::teams] for player in xrange(teams)]
        listresult.append(game)
        
    
   # game = [list(players[player::teams]) for player in xrange(teams)]

    return game
    
    
    


    
    """for index, player in enumerate(players):
        for index2, player2 in enumerate(players):
            player2 = players[teams]
            listresult.append([player, player2])"""


    


    
        
PLIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1),
           ('g', 1), ('h', 0), ('i', 1)]
print matchmaking(PLIST)
