# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:27 2020

@author: Manda Jensen (mp-jensen)
"""

import testUtility


#Set the player names
player_names = ["Annie","*Ben","*Carla"]

#get the card box
box = testUtility.getBox(player_names)

#get the card supply for this specific game
supply = testUtility.getSupply(box, player_names)

#get the player objects
players = testUtility.getPlayers(player_names)

#Play the game
testUtility.playGame(supply,players)         

#Calculate and print the final score
testUtility.scoreGame(players)
