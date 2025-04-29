from .pkmn import pkmn
from .attack import attack
from .pkmnAtk import pkmnAtk
class activepkmn: 
    def __init__(self,
  pkmn: pkmn,
  currentHP:int,
  ID:int,
  attack1: pkmnAtk,
  attack2: pkmnAtk,
  attack3: pkmnAtk,
  attack4: pkmnAtk, 
  name:str= "",
  level:int = 100,
  item = None,
  state: [None, "burn", "freeze", "paralysed", "poison", "badly poison"] = None,
  bonuses: dict={"crit":0, "Atk": 0, "Def":0,"SpA":0,"SpD":0,"Speed":0,"Accuracy":0,"Evasines":0},
  
 ):
     self.pkmn = pkmn
     self.item = item
     self.state = state
     self.attack1 = attack1
     self.attack2 = attack2
     self.attack3 = attack3
     self.attack4 = attack4
     self.level = level
     self.currentHP = currentHP
     self.bonuses = bonuses
     self.id = ID
     if name == "":
      self.name = pkmn.name
     else:
      self.name = name
     if pkmn.Type1 == "Flying" or pkmn.Type2 == "Flying":
      self.grounded = False
     else:
      self.grounded = True
   