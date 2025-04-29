from .userFieldCond import userFieldCond
from .weather import listAura,listTerrain,listWeather
from .userparty import userParty
class weather:
  def __init__(self,name:listWeather,turnLeft: int):
    self.name = name
    self.turnLeft = turnLeft

class terrain:
  def __init__(self,name:listWeather,turnLeft: int):
    self.name = name
    self.turnLeft = turnLeft

class match :
    def __init__(self,
  user1: int,
  user2: int,
  user1Party: userParty,
  user2Party: userParty,
  user1FieldCond: userFieldCond,
  user2FieldCond: userFieldCond,
  weather: weather= weather(None,0),
  aura: listAura = None,
  terrain:terrain = weather(None, 0), ):
     self.user1 = user1
     self.user2 = user2
     self.user1FieldCond= user1FieldCond
     self.user2FieldCond = user2FieldCond
     self.weather = weather
     self.aura =aura
     self.terrain = terrain
