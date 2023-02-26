import CurrencyRouletteGame
import GuessGame
import MemoryGame


def welcome():
    name = input("""*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
    Welcome, please enter your name:""")
    return f"""
    Hello {name.capitalize()} and welcome to the World of Games (WoG).
    Here you can find many cool games to play."""

###get_difficulty is a function that checks the input

def get_difficulty():
  try:
    number = int(input("""*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
    Please choose game difficulty from 1 to 5:
"""))
    if 0 < number < 6:
        if number == 1:
            print ("Easy")
        elif number == 2:
            print ("Medium")
        elif number == 3:
               print ("Hard")
        elif number == 4:
               print ("Insane")
        else:
               print ("Insane")
    else:
         print('Please choose a valid option\n')
         get_difficulty()
  except ValueError:
      print("The provided value is not an integer")
      get_difficulty()
  return number

##load_game is a function that loads the game
def load_game():

    print("""*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    2. Guess Game - guess a number and see if you chose like the computer")
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    try:
        game_number = int(input())
        if 0 < game_number < 4:
            if game_number == 1:
                print("The Memory Game: A sequence of numbers will appear for 1 second, and you have to guess it back.")
                MemoryGame.play(get_difficulty())
            elif game_number == 2:
                print("The Guessing Game: Guess a number and see if you choose like the computer.")
                GuessGame.play(get_difficulty())
            elif game_number == 3:
                print("The Currency Roulette Game: Try and guess the value of a random amount of USD in ILS.")
                CurrencyRouletteGame.play(get_difficulty())
        else:

            print("""*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
            please enter a number and try again""")
            load_game()
    except ValueError:
            print("""*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
            The provided value is not an integer""")
            load_game()
