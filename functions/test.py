from classes.attack import attack
from classes.pkmn import pkmn
from classes.activepkmn import activepkmn
from classes.userFieldCond import userFieldCond
from classes.match import match
from .decisionMaking import DecisionMaking
from classes.pkmnAtk import pkmnAtk
from .order_action import order_action
from classes.userparty import userParty
from .getBaseDamage import getbaseDamage
from .applyModifiers import applyModifiers
from classes.match import weather
import pickle


blizzard_db = attack(priority=0,BP=110,accuracy=70, contact=False,effect=None,Ptype="Ice",style="special", nom="Blizzard",PP=8)
flamethrower_db= attack(priority=0,BP=90,accuracy=100, contact=False,effect=None,Ptype="Fire",style="special", nom="Flamethrower",PP=16)

Abomasnow= pkmn(HP=383, Atk=198,Def=273, SpA=220,SpD=206,Speed=158,Skill="Swow Warning",Type1="Ice",Type2="Grass", name="Abomasnow")
Charizard= pkmn(HP=297, Atk=155,Def=192, SpA=317,SpD=207,Speed=328,Skill="Blaze",Type1="Fire",Type2="Flying", name="Charizard")

Blizzard = pkmnAtk(attack=blizzard_db,PPleft=blizzard_db.PP)
Flamethrower = pkmnAtk(attack=flamethrower_db, PPleft=flamethrower_db.PP)
myAbomasnow = activepkmn(
    ID=1,
    pkmn=Abomasnow,
    attack1=Blizzard,
     attack2=Blizzard,
     attack3=Blizzard,
     attack4=Blizzard,
     currentHP=Abomasnow.HP,
     name="MyAbom"
     )
myCharizard=activepkmn(
    ID=2,
    pkmn=Charizard,
    attack1=Blizzard,
     attack2=Blizzard,
     attack3=Blizzard,
     attack4=Blizzard,
     currentHP=Abomasnow.HP,
     name="Tutura2"
     )

yourAbomasnow= activepkmn(
    ID= 3,
    pkmn=Abomasnow,
    attack1=Blizzard,
     attack2=Blizzard,
     attack3=Blizzard,
     attack4=Blizzard,
     currentHP=Abomasnow.HP,
     name="YourAbom"

     )
yourCharizard=activepkmn(
    ID=4,
    pkmn=Charizard,
    attack1=Blizzard,
     attack2=Blizzard,
     attack3=Blizzard,
     attack4=Blizzard,
     currentHP=Abomasnow.HP,
     name="Tutura3"
     )
user1Party = userParty(myAbomasnow,myCharizard,myAbomasnow,myAbomasnow,myAbomasnow,myAbomasnow)
user2Party = userParty(yourAbomasnow,yourAbomasnow,yourCharizard,yourAbomasnow,yourAbomasnow,yourAbomasnow)

myfieldCond= userFieldCond(activePkmn=myAbomasnow)
yourFieldCOnd= userFieldCond(activePkmn=yourAbomasnow)

myMatch = match(user1=1,user2=2,user1FieldCond=myfieldCond,user2FieldCond=yourFieldCOnd,
user1Party=user1Party, user2Party=user2Party, weather=weather("Rain",1))


   
def tour(match:match):
    actionUser1 = DecisionMaking(match.user1FieldCond.activePkmn,userParty=user1Party)
    actionUser2 = DecisionMaking(match.user2FieldCond.activePkmn, userParty=user2Party)
    order_action(pkmnUser1=match.user1FieldCond.activePkmn,actionUser1=actionUser1,
    pkmnUser2=match.user2FieldCond.activePkmn,actionUser2=actionUser2)
    
        

tour(match=myMatch)
# resultat =getbaseDamage(AttackingUser=myAbomasnow,targetFieldcond=myMatch.user2FieldCond,
#  usedAttack=myAbomasnow.attack1, aura=myMatch.aura, terrain=myMatch.terrain.name,
#  weather=myMatch.weather.name)
# isCrit = resultat["isCrit"]
# dmg = resultat["baseDamage"]
# realDmg = applyModifiers(basicdamage=dmg,AttackingUser=myAbomasnow,
# aura=None,weather=myMatch.weather.name,isCrit=isCrit,targetFieldcond=yourFieldCOnd,
# terrain=None,usedAttack=myAbomasnow.attack1)
# print(realDmg)
# applyModifiers(AttackingUser=myAbomasnow,aura=None,basicdamage=dmg,isCrit=isCrit,
# targetFieldcond=yourFieldCOnd,terrain=myMatch.terrain,
# usedAttack=myAbomasnow.attack1,weather=myMatch.weather)
# print(isCrit, dmg)
# with open("data/table_des_types.pkl", "rb") as file:
#     table_des_types = pickle.load(file)
#     file.close()

# toto = "Fire"
# print(table_des_types[toto])
