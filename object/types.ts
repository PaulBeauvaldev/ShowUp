export type type = [
  "???",
  "fire",
  "water",
  "grass",
  "ice",
  "fly",
  "poison",
  "ghost",
  "dark",
  "fairy",
  "dragon",
  "normal",
  "psy",
  "steel",
  "insect",
  "electrik",
  "rock",
  "ground",
  "fight",
  "stellar"
];
export type pkmn = {
  HP: number;
  atk: number;
  def: number;
  spAtk: number;
  spDef: number;
  speed: number;
  skill: (self) => void;
  type1: type;
  type2: null | type;
};
export type weather = [
  "sun",
  "rain",
  "primalSun",
  "primalRain",
  "sandstorm",
  "hail",
  null
];
export type aura = ["fairy", "dark", "break", "fairybreak", "darkbreak", null];
export type terrain = ["elec", "grassy", "psychic", "mysti", null];
export type activepkmn = {
  pkmn: pkmn;
  item: (self) => void;
  confused: boolean;
  state: [null, "burn", "freeze", "paralysed", "poison", "badly poison"];
  bonuses: {
    HP: number;
    atk: number;
    def: number;
    spAtk: number;
    spDef: number;
    speed: number;
    precision: number;
    evasiness: number;
  };
  attack1: attack;
  attack2: attack;
  attack3: attack;
  attack4: attack;
};
export type attack = {
  priority: number;
  BP: number;
  contact: boolean;
  style: ["effect", "physical", "special"];
  accuracy: number;
  type: type;
  effect: (self) => void;
};
export type userFieldCond = {
  stealthRock: boolean;
  spike: number;
  tspike: number;
  sticky: boolean;
  reflect: number;
  lightscreen: number;
  activePkmn: activepkmn;
};
export type user = { nom: string };
export type match = {
  user1: user;
  user2: user;
  user1FieldCond: userFieldCond;
  user2FieldCond: userFieldCond;
  weather: { name: weather; turnLeft: number };
  aura: aura;
  terrain: terrain;
};
