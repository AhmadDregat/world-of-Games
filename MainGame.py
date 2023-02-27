from Live import load_game, welcome
print(welcome())
load_game()
ask_user=input ("""Did you want to go to the games list?
if yes, please enter Y, otherwise press any key to exit.
 """)
if (ask_user=="Y" or ask_user=="y"):
    print("welcome again:)")
    load_game()
else:
    print("Goodbye!")