from random import choice
from turtle import Turtle

class TurtleRace:
    def __init__(self): # source of truth stays in
        self.turtle = ''
        self.total = 50
        self.bet = 0
        
    def keep_or_choose(self):
        if self.turtle != '':
            keep = input('Would you like to keep your previous turtle? (y/n): ')
            if keep.lower() == 'y':
                print('Keeping %s as your turtle.' % self.turtle)
            elif keep.lower() == 'quit':
                quit()
            elif keep.lower() == 'n':
                self.chooseTurtle()
            else:
                print('Please type y or n!')
                self.keep_or_choose()
        else: self.chooseTurtle()
    
    def chooseTurtle(self):
        active = True
        while active:
            turtle = input('Inky (17%s chance to win)\nBlinky (22%s chance to win)\nPinky (28%s chance to win)\nClyde (33%s chance to win)\nPlease choose your turtle!: ')
            if turtle.lower() == 'i' or turtle.lower() == 'inky':
                self.turtle = 'Inky'
                active = False
            elif turtle.lower() == 'b' or turtle.lower() == 'blinky':
                self.turtle = 'Blinky'
                active = False
            elif turtle.lower() == 'p' or turtle.lower() == 'pinky':
                self.turtle = 'Pinky'
                active = False
            elif turtle.lower() == 'c' or turtle.lower() == 'clyde':
                self.turtle = 'Clyde'
                active = False
            elif turtle.lower() == 'quit':
                quit()
            else:
                print('Valid replies include: Inky, Blinky, Pinky, Clyde, I, B, P, C, or quit')
                continue
    
    def setBet(self):
        active = True
        while active:
            bet = input('You chose: ' + self.turtle + '\nOf %s, how much would you like to bet? ' % self.total)
            if bet == 'quit':
                quit()
            else:
                bet = int(bet)
                
                if bet < 1:
                    print('Cannot bet zero or less! ')
                    continue
                elif bet == 'quit':
                    quit()
                elif bet > self.total:
                    print('Cannot bet more than you have! You have: %s' % self.total)
                    continue
                
            self.bet = bet
            
            confirm = input('Betting %s. Are you sure? (y/n): ' % self.bet)
            if confirm == 'n':
                continue
            elif confirm == 'y':
                active = False
            elif bet == 'quit':
                quit()
            else:
                print('Please type y or n: ')
                continue
        
    def race(self):
        names = ['Inky', 'Blinky', 'Pinky', 'Clyde']
        results = {}
        result_names = []
        for name in names:
            results[Turtle(name).name] = Turtle(name).time
            
        order = dict(sorted(results.items(), key=lambda item: item[1]))
        
        for item in order.keys():
            result_names.append(item)
            
        print('The results are in!')
        
        for x, y in order.items():
            print(x + ': ' + str(y) + ' seconds')
        
        print('Winner: ' + result_names[0])
        
        if result_names[0] == self.turtle:
            self.award_winnings()
        else: print('Sorry, your chosen turtle (' + self.turtle + ') lost.')
        
        
    def award_winnings(self):
        amount = 0
        if self.turtle == 'Inky':
            amount = round(self.bet * 5.21, 3)
        elif self.turtle == 'Blinky':
            amount = round(self.bet * 4.50, 3)
        elif self.turtle == 'Pinky':
            amount = round(self.bet * 3.54, 3)
        elif self.turtle == 'Clyde':
            amount = round(self.bet * 3, 3)
        
        self.total = self.total + amount
        
        print('You won %s!' % amount)
        print('Your total is now %s.' % self.total)
        
# 5.21 Inky
# 4.50 Blinky
# 3.54 Pinky
# 3 Clyde