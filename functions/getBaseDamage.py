from classes.activepkmn import activepkmn
from classes.pkmnAtk import pkmnAtk
from classes.userFieldCond import userFieldCond
from .applyBonus import applyBonus
from classes.weather import listTerrain, listWeather,listAura
import random
from math import floor
def getbaseDamage(AttackingUser: activepkmn, usedAttack: pkmnAtk,weather: listWeather,
aura: listAura,terrain: listTerrain,targetFieldcond: userFieldCond):
        if usedAttack.attack.style == "effect":
            1
        else:
            critbonus= 1
            match AttackingUser.bonuses["crit"]:
                case 1:
                    critrate = 8
                case 2:
                    critrate = 2
                case 3:
                    critrate= 1
                case _: 
                    critrate= 24
            roll = random.uniform(0,1)
            isCrit = (1/critrate)> roll
            if usedAttack.attack.style == "physical":
                if isCrit:
                    currentTargetDef = applyBonus(bonus=min(targetFieldcond.activePkmn.bonuses["Def"],0),
                    stat= targetFieldcond.activePkmn.pkmn.Def)
                    currentUserAtk = applyBonus(bonus=max(AttackingUser.bonuses["Atk"],0),stat= AttackingUser.pkmn.Atk)
                else:
                    if AttackingUser.state == "burn":
                        currentUserAtk = applyBonus(bonus=AttackingUser.bonuses["Atk"], stat=AttackingUser.pkmn.Atk)/2
                    else:
                        currentUserAtk = applyBonus(bonus=AttackingUser.bonuses["Atk"],stat=AttackingUser.pkmn.Atk)
                    currentTargetDef = applyBonus(bonus=targetFieldcond.activePkmn.bonuses["Def"], 
                    stat=targetFieldcond.activePkmn.pkmn.Def)
                damageWithoutContext= (((2*AttackingUser.level/5)+2)*usedAttack.attack.BP*(currentUserAtk/currentTargetDef)/50)+2
                return({isCrit:isCrit, damageWithoutContext: damageWithoutContext})

                ###SPE ATK
            if usedAttack.attack.style == "special":
                currentTargetDef = targetFieldcond.activePkmn.pkmn.SpD 
                if weather == "Sandstorm" and (targetFieldcond.activePkmn.pkmn.Type1 == "Rock" or 
            targetFieldcond.activePkmn.pkmn.Type2 == "Rock" ):
                    currentTargetDef = currentTargetDef * 1.5
                if isCrit:
                    currentTargetDef = applyBonus(bonus=min(targetFieldcond.activePkmn.bonuses["SpD"],0),
                    stat= currentTargetDef)
                    currentUserAtk = applyBonus(bonus=max(AttackingUser.bonuses["SpA"],0),stat= AttackingUser.pkmn.SpA)
                else:
                    currentUserAtk = applyBonus(bonus=AttackingUser.bonuses["SpA"],stat=AttackingUser.pkmn.SpA)
                    currentTargetDef = applyBonus(bonus=targetFieldcond.activePkmn.bonuses["SpD"], 
                    stat=targetFieldcond.activePkmn.pkmn.SpD)
                baseDamage= floor((((2*AttackingUser.level/5)+2)*usedAttack.attack.BP*(currentUserAtk/currentTargetDef)/50)+2)
                # if pkmnAtk.attack.
                return({"isCrit":isCrit, "baseDamage": baseDamage})
            