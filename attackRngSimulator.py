"""
@author Tucker Ferguson
1/6/2020
---------------------------------------------------------------------------------
Simulates random number generation damage using python collections and Modules  |
---------------------------------------------------------------------------------
1) For simulation simply input nothing the move and rng will be chosen for you

2) However Entering a move from the 'moveList' will yield its corresponding damage done 


-P.S. this is part of something much much grander im working on :)
"""
import random
import re

#For this exaple only Attack will be used
inputList = ["Run","Attack","Bag"]


#Contains available moves to be used
moveList = ["Fireball", "Bolt", "Waterfall", "Blizz"]

#prompts the user for battle!!! 
print("""
Choose your move:
                 **************************
                 * {0}         {1}  *
                 * {2}        {3} *
                 **************************
""".format(moveList[0],moveList[1],moveList[2],moveList[3]))

#@param: inputList here is hardcoded to demonstrate only attack option                              
#        prompt can either be a move from the list for nothing
def moveOp(inputList,prompt) :
    choice = inputList[1]
    if choice in actionDict :
        move = actionDict[choice]
        move(prompt)

#Future implementation (breaks out of battle)                
def run():
    print("Run with a swiftness!")


#@param prompt is the uesrs choice in moves, or the randomly chosen one
#uses the random module to simulate damage being dealt
def attack(prompt):
    dmgRng = random.randint(0,100)
    if prompt in moveList :
        move = prompt
    else :
        move = moveList[random.randint(0,2)]
    if(dmgRng == 0):
        print("you missed!")
    elif(dmgRng > 70) :
        print("{0} did {1} damage! critical hit!".format(move,dmgRng))
    elif(dmgRng < 30):
         print("{0} did {1} damage! not a very effective hit!".format(move,dmgRng))
    else :
        print("{0} did {1} damage!".format(move,dmgRng))

#future implementation    
def bag() :
    return

#Dictionary used to store reference to helper functions
actionDict = {
    "Run":run,
    "Attack":attack,
    "Bag":bag,
}

#User input is processed here using the regular expression module
prompt = input()
pattern = '[A-z]+'
if(prompt != None) :
    if(re.match(pattern,prompt)) :
        moveOp(inputList,prompt)  
    else :
        moveOp(inputList,"")
     #assert(prompt in moveList != True),"This move is unknown..."
                                              