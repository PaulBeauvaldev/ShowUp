import pickle
def applyTypesBonuses(basedamage:int,attackType: str,pkmnType1:str,pkmnType2:str):
    with open("data/table_des_types.pkl", "rb") as file:
        table_des_types = pickle.load(file)
        file.close()

    finaldamage = basedamage * table_des_types[attackType][pkmnType1] * table_des_types[attackType][pkmnType2]
    return finaldamage