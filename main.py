from turtlerace import TurtleRace

print('Welcome to TurtleRace!')
print('Place your bet on a turtle to win.\nYou start with 50 and can bet as much as you have.')
print('Type "quit" to exit the game.')

tr = TurtleRace()

active = True
while active:

    tr.keep_or_choose() # three parts - 1) pick turtle
    tr.setBet() # 2) place bet
    tr.race() # 3) race