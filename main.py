from tables import *


class Modifier:
    def __init__(self, positive, percentage):
        self.positive = positive
        self.percentage = percentage


def determine_number_of_couples_modifier(n):
    if n < 24:
        positive = False
    else:
        positive = True

    if n < 7:
        percentage = 30
    elif n < 12:
        percentage = 20
    elif n < 24:
        percentage = 10
    elif n < 36:
        percentage = 0
    elif 36 <= n < 48:
        percentage = 10
    elif n < 96:
        percentage = 25
    elif n < 144:
        percentage = 30
    elif n < 192:
        percentage = 35
    elif n < 288:
        percentage = 40
    else:
        percentage = 50

    return Modifier(positive, percentage)


def determine_top_12_modifier(n):
    percentage = 0
    if n > 9:
        percentage = 70
    elif n > 6:
        percentage = 50
    return Modifier(True, percentage)


def determine_top_24_modifier(n):
    percentage = 0
    if n > 9:
        percentage = 35
    elif n > 6:
        percentage = 25
    return Modifier(True, percentage)


def determine_top_36_modifier(n):
    percentage = 0
    if n > 6:
        percentage = 10
    return Modifier(True, percentage)


def determine_countries_modifier(n):
    percentage = 0
    if n > 23:
        percentage = 50
    elif n > 15:
        percentage = 40
    elif n > 10:
        percentage = 25
    elif n > 7:
        percentage = 10
    return Modifier(True, percentage)


# wtf
def determine_judge_modifier(n_judges, n_countries):
    percentage = 0
    if n_countries > 10:
        percentage = 30
    elif n_countries > 8:
        percentage = 25
    elif n_judges == 9 & n_countries == 8:
        percentage = 15
    elif n_countries > 6:
        percentage = 15
    return Modifier(True, percentage)


def get_base_table_for_comp_type(comp_type):
    if comp_type == 0:
        return grandSlamTable
    if comp_type == 1:
        return worldOpenTable
    if comp_type == 2:
        return internationalOpenTable
    return openTable


def apply_modifiers(base_table, modifiers):
    return 0


if __name__ == '__main__':
    compType = 0
    numberOfCouples = 0
    numberOfCouplesTop12 = 0
    numberOfCouplesTop24 = 0
    numberOfCouplesTop36 = 0
    coupleCountries = 0
    numberOfJudges = 0
    judgeCountries = 0

    numberOfCouplesModifier = determine_number_of_couples_modifier(numberOfCouples)
    top12Modifier = determine_top_12_modifier(numberOfCouplesTop12)
    top24Modifier = determine_top_24_modifier(numberOfCouplesTop24)
    top36Modifier = determine_top_36_modifier(numberOfCouplesTop36)
    countriesModifier = determine_countries_modifier(coupleCountries)
    judgeModifier = determine_judge_modifier(numberOfJudges, judgeCountries)

    modifierList = [
        numberOfCouplesModifier,
        top12Modifier,
        top24Modifier,
        top36Modifier,
        countriesModifier,
        judgeModifier
    ]

    baseTable = get_base_table_for_comp_type(compType)

    pointsTable = apply_modifiers(baseTable, modifierList)
