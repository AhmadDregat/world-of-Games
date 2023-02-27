import math
import random
from currency_converter import CurrencyConverter

from Score import add_score


def get_money_interval():
    rand_number = random.randrange(1, 100)
    t=CurrencyConverter().convert(rand_number, 'USD', 'ILS')
    print(f'Please enter number,\nHow much {rand_number} is worth in shekels:')
    print(t)
    return t
def get_guess_from_user(t, difficulty):
    try:
        guss_user = int(input())
        if  abs(t-(10-difficulty)) < guss_user < abs(t+(10-difficulty)):
            return True
        else:
            print('sorry wrong!!, Please try again')
            return False

    except ValueError:
        print("The provided value is not an integer")
        get_guess_from_user()
def play(difficulty):
    if get_guess_from_user(get_money_interval(), difficulty) == False:
        print('sorry wrong!!, Please try again')
        play(difficulty)
        return False
    else:
        print('Congratulations!!')
        add_score(difficulty)
        play(difficulty)
        return True

