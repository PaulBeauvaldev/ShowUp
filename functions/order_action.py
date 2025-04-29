from classes import activepkmn
from classes.pkmnAtk import pkmnAtk
from classes import attack
from .applyBonus import applyBonus

def order_action(pkmnUser1: activepkmn,pkmnUser2: activepkmn, actionUser1:str, actionUser2: str):
    if (type(actionUser1)== pkmnAtk and type(actionUser2)== pkmnAtk):
        if (actionUser1.attack.priority >actionUser2.attack.priority):
                "print(user 1 puis user 2) par priorité"
        elif(actionUser1.attack.priority <actionUser2.attack.priority):
                "print(user 2 puis user 1) par priorité"
        else:
            ###calculating speed
            user1Speed= applyBonus(pkmnUser1.bonuses["Speed"],pkmnUser1.pkmn.Speed)
            if pkmnUser1.state == "paralysed":
                user1Speed = user1Speed/2
            user2Speed= applyBonus(pkmnUser2.bonuses["Speed"],pkmnUser2.pkmn.Speed)
            if pkmnUser2.state == "paralysed":
                user2Speed = user2Speed/2

            ###comparing speed
            if user1Speed > user2Speed:
                print("user 1 puis user 2 par speed")
            elif user1Speed < user2Speed:
                print("user 2 puis user 1 par speed")
            else:
                print("speedTie")


    elif(type(actionUser1)!= pkmnAtk and type(actionUser2)== pkmnAtk):
        print("j1 switch puis bagarre")
    elif(type(actionUser1)== pkmnAtk and type(actionUser2)!= pkmnAtk):
        print("j2 switch puis bagarre")
    elif(type(actionUser1)!= pkmnAtk and type(actionUser2)!= pkmnAtk):
        user1Speed= applyBonus(pkmnUser1.bonuses["Speed"],pkmnUser1.pkmn.Speed)
        if pkmnUser1.state == "paralysed":
            user1Speed = user1Speed/2
        user2Speed= applyBonus(pkmnUser2.bonuses["Speed"],pkmnUser2.pkmn.Speed)
        if pkmnUser2.state == "paralysed":
            user2Speed = user2Speed/2

        ###comparing speed
        if user1Speed > user2Speed:
            print("user 1 puis user 2 par speed")
        elif user1Speed < user2Speed:
            print("user 2 puis user 1 par speed")
        else:
            print("speedTie")
        print("Double switch")
    