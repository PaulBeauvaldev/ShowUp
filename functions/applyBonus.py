def applyBonus(bonus: int, stat: int):
    match bonus:
        case 0:
            return stat
        case 1:
            return stat*1.5
        case 2:
            return stat*2
        case 3:
            return stat * 2.5
        case 4:
            return stat * 3
        case 5:
            return stat * 3.5
        case 6:
            return stat * 4
        case -1:
            return stat*0.67
        case -2:
            return stat/2
        case -3:
            return stat * 0.4
        case -4:
            return stat/3
        case -5:
            return stat * (2/7)
        case -6:
            return stat/4
        case _:
            if bonus>6:
                return stat * 4
            elif bonus<-6:
                return stat/4
            else:
                return stat