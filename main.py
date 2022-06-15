from turtlerace import TurtleRace

print('Welcome to TurtleRace!')
print('Place your bet on a turtle to win.\nYou start with 50 and can bet as much as you have.')
print('Type "quit" to exit the game.')
print('The four turtles are Inky, Blinky, Pinky, and Clyde.\nYou can type their name or just the first letter.')

active = True
while active:
    
    tr = TurtleRace()
    tr.chooseTurtle()
    tr.setBet()
    tr.race()
    
    again = input('Race again? (y/n): ')
    if again.lower() == 'y':
        continue
    elif again.lower() == 'n':
        active = False