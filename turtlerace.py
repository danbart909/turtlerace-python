from turtle import Turtle

class TurtleRace:
    def __init__(self):
        self.turtle = ''
        self.total = 50
        self.bet = 0
        
    def keep_or_choose(self):
        if self.turtle != '':
            keep = input('Would you like to keep your selected turtle in the next race? (y/n): ')
            if keep.lower() == 'y':
                print('Keeping ' + self.turtle + ' as your turtle.')
            elif keep.lower() == 'n':
                self.chooseTurtle()
            else:
                print('Please type y or n!')
                self.keep_or_choose()
        else: self.chooseTurtle()
    
    def chooseTurtle(self):
        active = True
        while active:
            turtle = input('The four turtles are Inky, Blinky, Pinky, and Clyde.\nYou can type their name or just the first letter.\nInky (17% chance to win)\nBlinky (22% chance to win)\nPinky (28% chance to win)\nClyde (33% chance to win)\nPlease choose your turtle: ')
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
            else:
                print('Valid replies include: Inky, Blinky, Pinky, Clyde, I, B, P, C, or quit()')
                continue
        print('You chose: ' + self.turtle)
    
    def setBet(self):
        active = True
        while active:
            bet = input('Of ' + self.total + ', how much would you like to bet? ')
            bet = int(bet)
            
            if bet < 1:
                print('Cannot bet zero or less! ')
                continue
            elif bet > self.total:
                print('Cannot bet more than you have! You have: ' + self.total)
                continue
            
            self.bet = bet
            
            confirm = input('Betting ' + self.bet + '. Are you sure? (y/n): ')
            if confirm == 'n':
                active = False
                self.unsure()
            elif confirm == 'y':
                active = False
            else:
                print('Please type y or n: ')
                continue
    
    def unsure(self):
        choose = input('Unsure about your turtle or your bet? Type "turtle", "bet", or "nevermind": ')
        if choose.lower() == 'turtle':
            self.chooseTurtle()
        elif choose.lower() == 'bet':
            self.setBet()
        elif choose.lower() == 'nevermind':
            self.race()
        else: print('Please type either "turtle", "bet", or "nevermind": ')
        
    def race(self):
        names = ['Inky', 'Blinky', 'Pinky', 'Clyde']
        results = {}
        result_names = []
        for name in names:
            results[Turtle(name).name] = Turtle(name).time
            
        order = dict(sorted(results.items(), key=lambda item: item[1]))
        
        for item in order.keys():
            result_names.append(item)
        
        print('Look at them go!\nThe results are in!')
        
        for x, y in order.items():
            print(x + ': ' + str(y) + ' seconds')
        
        print('Winner: ' + result_names[0])
        
        if result_names[0] == self.turtle:
            self.award_winnings()
        else:
            self.total -= self.bet
            print('Sorry, your chosen turtle (' + self.turtle + ') lost.')
        
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
        
        self.total += amount
        
        print('You won ' + amount + '!\nYour total is now ' + self.total + '.')