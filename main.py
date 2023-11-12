from tables import *


def determine_number_of_couples_modifier(n):

    if n < 7:
        return -30
    elif n < 12:
        return -20
    elif n < 24:
        return -10
    elif n < 36:
        return 0
    elif 36 <= n < 48:
        return 10
    elif n < 96:
        return 25
    elif n < 144:
        return 30
    elif n < 192:
        return 35
    elif n < 288:
        return 40
    else:
        return 50


def determine_top_12_modifier(n):
    if n > 9:
        return 70
    elif n > 6:
        return 50
    return 0


def determine_top_24_modifier(n):
    if n > 9:
        return 35
    if n > 6:
        return 25
    return 0


def determine_top_36_modifier(n):
    if n > 6:
        return 10
    return 0


def determine_countries_modifier(n):
    if n > 23:
        return 50
    if n > 15:
        return 40
    if n > 10:
        return 25
    if n > 7:
        return 10
    return 0


# wtf
def determine_judge_modifier(n_judges, n_countries):
    if n_countries > 10:
        return 30
    if n_countries > 8:
        return 25
    if n_judges == 9 & n_countries == 8:
        return 15
    if n_countries > 6:
        return 15
    return 0


def get_base_table_for_comp_type(comp_type):
    if comp_type == 0:
        return grandSlamTable
    if comp_type == 1:
        return worldOpenTable
    if comp_type == 2:
        return internationalOpenTable
    return openTable


def calculate_table(base_table, modifiers, numer_of_couples):
    result = {}

    for i in range(numer_of_couples):
        base_points = base_table.get(i + 1)
        if base_points is None:
            base_points = base_table.get(len(base_table))
        additional_points = 0
        for modifier in modifiers:
            additional_points += base_points * (modifier / 100)
        result[i + 1] = base_points + additional_points

    return result


if __name__ == '__main__':
    compType = 2
    numberOfCouples = 21
    numberOfCouplesTop12 = 0
    numberOfCouplesTop24 = 0
    numberOfCouplesTop36 = 1
    coupleCountries = 6
    numberOfJudges = 11
    judgeCountries = 10
    
    modifierList = [determine_number_of_couples_modifier(numberOfCouples),
                    determine_top_12_modifier(numberOfCouplesTop12),
                    determine_top_24_modifier(numberOfCouplesTop24),
                    determine_top_36_modifier(numberOfCouplesTop36),
                    determine_countries_modifier(coupleCountries),
                    determine_judge_modifier(numberOfJudges, judgeCountries)]

    baseTable = get_base_table_for_comp_type(compType)

    pointsTable = calculate_table(baseTable, modifierList, numberOfCouples)
    for key in pointsTable.keys():
        print(str(key) + ": " + str(pointsTable[key]))
