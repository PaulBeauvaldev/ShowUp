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

global endTurn 
def tour(match:match):
    actionUser1 = DecisionMaking(match.user1FieldCond.activePkmn)
    actionUser2 = DecisionMaking(match.user2FieldCond.activePkmn)
    order_action(pkmnUser1=match.user1FieldCond.activePkmn,actionUser1=actionUser1,
    pkmnUser2=match.user2FieldCond.activePkmn,actionUser2=actionUser2)
    