from classes.userFieldCond import userFieldCond as usrFieldCond
from classes.activepkmn  import activepkm
from applyTypesBonuses import applyTypesBonuses
from applyDamage import applydamage
from math import floor
from classes.userparty import userParty
def applyEntryHazard(userFieldCond: usrFieldCond, userParty: userParty):
    if userFieldCond.activePkmn.state == None and userFieldCond.activePkmn.grounded:
        if userFieldCond.tspike == 1:
            if userFieldCond.activePkmn.pkmn.Type1 == "Poison" or  userFieldCond.activePkmn.pkmn.Type2 == "Poison":
                userFieldCond.tspike = 0
                print(f"{userFieldCond.activePkmn.name} has absorbed the toxic spike")
            else:
                userFieldCond.activePkmn.state = "poison"
                print(f"{userFieldCond.activePkmn.name} has been poinson by the toxic spike")
        elif userFieldCond.tspike >= 2:
            if userFieldCond.activePkmn.pkmn.Type1 == "Poison" or  userFieldCond.activePkmn.pkmn.Type2 == "Poison":
                userFieldCond.tspike = 0
                print(f"{userFieldCond.activePkmn.name} has absorbed the toxic spike")
            else:
                userFieldCond.activePkmn.state = "badly poison"
            print(f"{userFieldCond.activePkmn.name} has been badly poinson by the toxic spikes")
    if userFieldCond.stealthRock:
        stealthRockDamage = floor(applyTypesBonuses(switchedInPkmn.pkmn.HP/16))
        applydamage(userParty=userParty,dmg=stealthRockDamage,targetPkmn=userFieldCond.activePkmn)
    if userFieldCond.activePkmn.grounded:
        if userFieldCond.sticky and userFieldCond.activePkmn.currentHP>0:
           userFieldCond.activePkmn.bonuses["Speed"] = max(userFieldCond.activePkmn.bonuses["Speed"]-1, -6)
           
        if userFieldCond.spike ==1 and userFieldCond.activePkmn.currentHP>0: 
            spikeDmg = floor(switchedInPkmn.pkmn.HP/8)
            applydamage(userParty=userParty,dmg=spikeDmg,targetPkmn=userFieldCond.activePkmn)
        elif userFieldCond.spike ==2 and userFieldCond.activePkmn.currentHP>0: 
            spikeDmg = floor(switchedInPkmn.pkmn.HP/6)
            applydamage(userParty=userParty,dmg=spikeDmg,targetPkmn=userFieldCond.activePkmn)
        elif userFieldCond.spike >=3 and userFieldCond.activePkmn.currentHP>0: 
            spikeDmg = floor(switchedInPkmn.pkmn.HP/4)
            applydamage(userParty=userParty,dmg=spikeDmg,targetPkmn=userFieldCond.activePkmn)
        