from .activepkmn import activepkmn

class userFieldCond: 
    def __init__(self,
  activePkmn: activepkmn,
  stealthRock: bool = False,
  spike: int = 0,
  tspike: int = 0,
  sticky: bool= False,
  reflect: int = 0,
  lightscreen: int = 0,
  auroraveil: int = 0,
  

  ):
     self.activePkmn= activePkmn
     self.stealthRock = stealthRock
     self.spike = spike
     self.tspike = tspike
     self.sticky = sticky
     self.reflect = reflect
     self.lightscreen = lightscreen
     self.auroraveil = auroraveil