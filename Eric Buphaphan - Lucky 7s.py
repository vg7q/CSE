import random


def mon_mon(dice_1, dice_2, round, money, highest_round, highest_money):
    if money > 0:
        if highest_money < money:
            highest_money = money
            highest_round = round
        round += 1
        money -= 1
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        if dice_1 + dice_2 == 7:
            money += 5
            print("you finally have a 7 your very lucky")
            mon_mon(dice_1, dice_2, round, money, highest_round, highest_money)
        elif dice_1 + dice_2 != 7:
            print("sadly you don't have a 7 no lucky no money. The number was %d" % (dice_1 + dice_2))
            mon_mon(dice_1, dice_2, round, money, highest_round, highest_money)
    else: print("you have no money. took you %d rounds. Your highest amount of money "
                "was $%d at round %d" % (round, highest_money, highest_round))


mon_mon(0, 0, 0, 15, 0, 0)
