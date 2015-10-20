#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Midterm"""


def matchmaking(players): # teams=3, min_team=1, max_team=None):
    
    game = [player for player in players if player[1] == 1 ]
            

    return game
        
PLIST = [('a', 1), ('b', 1), ('c', 0), ('d', 1), ('e', 0), ('f', 1),
           ('g', 1), ('h', 0), ('i', 1)]
print matchmaking(PLIST)
