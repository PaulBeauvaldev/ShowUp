from .Ptypes import types

typeswithNone = types.append(None)
class pkmn:
    def __init__( self,
    HP: int,
    Atk: int,
    Def: int,
    SpA: int,
    SpD: int,
    Speed: int,
    name: str,
    Skill,
    Type1: types,
    Type2: types = None ):
        self.HP =HP
        self.Atk = Atk
        self.Def= Def
        self.SpA = SpA
        self.SpD = SpD
        self.Speed = Speed
        self.Skill = Skill
        self.Type1= Type1
        self.Type2 = Type2

