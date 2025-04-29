
from math import floor
from classes.userparty import userParty
from classes.activepkmn import activepkmn
def switchSelect(userkmn: activepkmn,userParty:userParty):
    print(f"""Please select a Poke:
    1#{userParty.pkmn1.name}: {userParty.pkmn1.currentHP}/{userParty.pkmn1.pkmn.HP}
    2#{userParty.pkmn2.name}: {userParty.pkmn2.currentHP}/{userParty.pkmn2.pkmn.HP}
    3#{userParty.pkmn3.name}: {userParty.pkmn3.currentHP}/{userParty.pkmn3.pkmn.HP}
    4#{userParty.pkmn4.name}: {userParty.pkmn4.currentHP}/{userParty.pkmn4.pkmn.HP}
    5#{userParty.pkmn5.name}: {userParty.pkmn5.currentHP}/{userParty.pkmn5.pkmn.HP}
    6#{userParty.pkmn6.name}: {userParty.pkmn6.currentHP}/{userParty.pkmn6.pkmn.HP}""")
    result = input("#")
    match result:
        case "1":
            if userParty.pkmn1.currentHP > 0:
                if userkmn != userParty.pkmn1:
                    return(userParty.pkmn1)
                else:
                    print(f"{userParty.pkmn1.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn1.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case "2":
            if userParty.pkmn2.currentHP > 0:
                if userkmn != userParty.pkmn2:
                    return(userParty.pkmn2)
                else:
                    print(f"{userParty.pkmn2.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn2.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case "3":
            if userParty.pkmn3.currentHP > 0:
                if userkmn != userParty.pkmn3:
                    return(userParty.pkmn3)
                else:
                    print(f"{userParty.pkmn3.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn3.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case "4":
            if userParty.pkmn4.currentHP > 0:
                if userkmn != userParty.pkmn4:
                    return(userParty.pkmn4)
                else:
                    print(f"{userParty.pkmn4.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn4.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case "5":
            if userParty.pkmn5.currentHP > 0:
                if userkmn != userParty.pkmn5:
                    return(userParty.pkmn5)
                else:
                    print(f"{userParty.pkmn5.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn5.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case "6":
            if userParty.pkmn6.currentHP > 0:
                if userkmn != userParty.pkmn6:
                    return(userParty.pkmn6)
                else:
                    print(f"{userParty.pkmn6.name} is already on the field")
                    return switchSelect(userkmn=userkmn,userParty=userParty)
            else:
                print(f"{userParty.pkmn6.name} is KO")
                return switchSelect(userkmn=userkmn,userParty=userParty)
        case _:
            print("Something went wrong, please retry")
            return switchSelect(userkmn=userkmn,userParty=userParty)