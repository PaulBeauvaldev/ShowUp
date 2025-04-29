from classes.userparty import userParty
from classes.activepkmn import activepkmn
 
def applydamage(targetPkmn: activepkmn,dmg:int,userParty: userParty):
    if targetPkmn.currentHP >0:
        match targetPkmn.id:
            case userParty.pkmn1.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn1.currentHP = targetPkmn.currentHP
            case userParty.pkmn2.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn2.currentHP = targetPkmn.currentHP
            case userParty.pkmn3.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn3.currentHP = targetPkmn.currentHP
            case userParty.pkmn4.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn4.currentHP = targetPkmn.currentHP
            case userParty.pkmn5.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn5.currentHP = targetPkmn.currentHP
            case userParty.pkmn6.id:
                targetPkmn.currentHP = max(0,targetPkmn.currentHP-dmg)
                userParty.pkmn6.currentHP = targetPkmn.currentHP
            case _:
                print("un pb détecté")
        if targetPkmn.currentHP <=0:
            print(f"{targetPkmn.pkmn.name} has fainted")
