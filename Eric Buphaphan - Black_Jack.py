import random


def Nom_Nom (Card_1, Card_2, round,)
   Card_1 = random.randint (1,11)
   Card_2 = random.randint (1,11)
        if Card_1 + Card_2 == 21:
            print ("You got a 21 congrats")
            Nom_Nom (Card_1, Card_2, round,)
        elif Card_1 + Card_2 !=21:
            print ("Sadly you dont have a 21. You had %d" % (Card_1 + Card_2))