from classes import activepkmn
from .switchSelect import switchSelect
from classes.userparty import userParty
def DecisionMaking(activePkmn:activepkmn, userParty: userParty):

    action = input(f"""Enter s to switch,
     1 to use {activePkmn.attack1.attack.nom} {activePkmn.attack1.PPleft}/{activePkmn.attack1.attack.PP},
     2 to use {activePkmn.attack2.attack.nom} {activePkmn.attack2.PPleft}/{activePkmn.attack2.attack.PP},
     3 to use {activePkmn.attack3.attack.nom} {activePkmn.attack3.PPleft}/{activePkmn.attack3.attack.PP},
     4 to use {activePkmn.attack4.attack.nom} {activePkmn.attack4.PPleft}/{activePkmn.attack4.attack.PP}, 
     #""")
    match action:
        case "1":
            if activePkmn.attack1.PPleft>0:
                return activePkmn.attack1
            print("No PP left, choose something else")
            return (DecisionMaking(activePkmn=activePkmn))
        case "2":
            if activePkmn.attack1.PPleft>0:
                return activePkmn.attack1
            print("No PP left, choose something else")
            return (DecisionMaking(activePkmn=activepkmn))
        case "3":
            if activePkmn.attack1.PPleft>0:
                return activePkmn.attack1
            print("No PP left, choose something else")
            return (DecisionMaking(activePkmn=activepkmn))
        case "4":
            if activePkmn.attack1.PPleft>0:
                return activePkmn.attack1
            print("No PP left, choose something else")
            return (DecisionMaking(activePkmn=activepkmn))
        case "s":
            
            return switchSelect(userkmn=activePkmn,userParty=userParty)
        case _ :
            print("toto")
            return
