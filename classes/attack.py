from .Ptypes import types
import random
from math import inf
from functions import applyBonus


class attack:
    def __init__(self,priority: int,
    BP:int,
    nom:str,
    contact:bool,
    accuracy: int,
    Ptype: types,
    effect,
    PP:int,
    style: ["physical","special","effect"]):
        self.priority =priority
        self.BP = BP
        self.contact = contact
        self.type = Ptype
        self.effect = effect
        self.style = style
        self.nom = nom
        self.PP = PP
                
                
