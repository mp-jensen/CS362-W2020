# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:27 2020

@author: Manda Jensen (mp-jensen)
"""

import Dominion
import random
from collections import defaultdict

#determine number of curses cards
def _getCurseNum(player_names):
    return -10 + 10 * len(player_names)

#determine the numer of victory cards
def _getVictoryNum(player_names):
    if len(player_names)>2:
        return 12
    else:
        return 8

#create a box and fill it with the correct cards
def getBox(player_names):
    nV = _getVictoryNum(player_names)
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

#create the supply order of each of the different types of cards
def _getSupplyOrder():
    return {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
            3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
            4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
            5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
            6:['Gold','Adventurer'],8:['Province']}

#choose 10 cards from the box to be in the supply, add the treasure, victory and curse cards and return the supply
def getSupply(box, player_names):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list,[(k,box[k]) for k in random10])
    #determine the victory and curse cards based on the number of players
    nV = _getVictoryNum(player_names)
    nC = _getCurseNum(player_names)
    #add the treasure, victory and curse cards, the supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC
    return supply


#get the player objects
def getPlayers(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

#play the game
def playGame(supply, players):
    #get the supply order
    supply_order = _getSupplyOrder()
    #initialize the trash
    trash = []
    #set the turn number
    turn  = 0
    while not Dominion.gameover(supply):
        turn += 1    
        print("\r")    
        for value in supply_order:
            print (value)
            for stack in supply_order[value]:
                if stack in supply:
                    print (stack, len(supply[stack]))
        print("\r")
        for player in players:
            print (player.name,player.calcpoints())
        print ("\rStart of turn " + str(turn))    
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players,supply,trash)
            

#Calculate and print final score
def scoreGame(players):
    dcs=Dominion.cardsummaries(players)
    vp=dcs.loc['VICTORY POINTS']
    vpmax=vp.max()
    winners=[]
    for i in vp.index:
        if vp.loc[i]==vpmax:
            winners.append(i)
    if len(winners)>1:
        winstring= ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0],'wins!'])

    print("\nGAME OVER!!!\n"+winstring+"\n")
    print(dcs)