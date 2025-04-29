from classes.activepkmn import activepkmn
import pickle
from classes.pkmnAtk import pkmnAtk
from classes.userFieldCond import userFieldCond
from .applyBonus import applyBonus
from classes.weather import listTerrain, listWeather,listAura
from random import randint
from math import floor
from .applyTypesBonuses import applyTypesBonuses

def applyModifiers(basicdamage:int,isCrit:bool,AttackingUser: activepkmn, 
usedAttack: pkmnAtk,weather: listWeather,
aura: listAura,terrain: listTerrain,targetFieldcond: userFieldCond):
    ### STAB
    if AttackingUser.pkmn.Type1 == usedAttack.attack.type or AttackingUser.pkmn.Type2 == usedAttack.attack.type:
        basicdamage = basicdamage*1.5
    ### Types
    

    basicdamage =applyTypesBonuses(attackType=usedAttack.attack.type,basedamage=basicdamage,
    pkmnType1=targetFieldcond.activePkmn.pkmn.Type1,pkmnType2=targetFieldcond.activePkmn.pkmn.Type2)
    
    #Aurora Veil   Reflect light screen and crit 
    if  not isCrit:
        #Reflect or Aura veil
        if (targetFieldcond.auroraveil > 0 or targetFieldcond.reflect > 0) and usedAttack.attack.style == "physical":
            basicdamage = basicdamage * 0.5
        #Reflect or Aura veil
        if (targetFieldcond.auroraveil > 0 or targetFieldcond.lightscreen > 0) and usedAttack.attack.style == "special":
            basicdamage = basicdamage * 0.5
    else:
        #crit is check so i apply crit here
        basicdamage = basicdamage * 1.5
    ### Apply weather
    input(weather)
    match weather:
        case "Sun":
            if usedAttack.attack.type == "Fire":
                 basicdamage = basicdamage * 1.5
            elif usedAttack.attack.type == "Water":
                basicdamage = basicdamage/2
        case "Rain":
            if usedAttack.attack.type == "Water":
                 basicdamage = basicdamage * 1.5
            elif usedAttack.attack.type == "Fire":
                basicdamage = basicdamage/2
        case _:
            next

                
    ###add randomiser
    basicdamage = (randint(85,100)*basicdamage)/100
    return floor(basicdamage)
            
        
    