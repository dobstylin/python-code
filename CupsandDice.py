
import random 

class sixSidedDie():
    def __init__(self):
        self.value = 0
        
    def roll(self):
        self.value = random.randint(1, 6)
        return (self.value)
        
    def getFaceValue(self):
        return(self.value)
        
    def __repr__(self):
        return('SixSidedDie({})'.format(self.value))

class tenSidedDie(sixSidedDie):
    def roll(self):
        self.value = random.randint(1, 10)
        return(self.value)
    
    def __repr__(self):
        return('TenSidedDie({})'.format(self.value))
        
class twentySidedDie(sixSidedDie):
    def roll(self):
        self.value = random.randint(1, 20)
        return(self.value)
    
    def __repr__(self):
        return('TwentySidedDie({})'.format(self.value))
    
class cup():
    def __init__(self, six=1, ten=1, twenty=1):
        self.total = 0
        self.cup = []
        for dice in range(0,six):
            self.cup.append(sixSidedDie())
        for dice in range(0,ten):
            self.cup.append(tenSidedDie())
        for dice in range(0,twenty):
            self.cup.append(twentySidedDie())
            
    def roll(self):
        self.total = 0
        for i in self.cup:
            self.total += i.roll()
        return self.total
    
    def getSum(self):
        return self.total
    
    def __repr__(self):
        return ('Cup('+','.join([str(d) for d in self.cup]) + ')')

def main():
    #call greeting function, greet user and ask their name
    name = greeting()
    #provide balance of 100 at the beginning
    balance = 100
    start = input('Do you want to play the game? y or n:')
    if start.lower() != 'y':
        print('Thank you {}, goodbye!'.format(name))
        return None
    while True:
        print('You have a balance of {}'.format(balance))
        goal = setGoal()
        #asks user how much they would like to bet, if negative program restarts
        bet = int(input('How much would you like to bet?'))
        if bet < 0:
            print('You cannot bet a negative amount, try again')
            return main()
        else: 
            #bet deducted from balance
            balance -= bet
            result = play()
            balance = calcBalance(result, goal, bet, balance)
            print('After your bet you now have a balance of ', balance)
            replay = input('Would you like to play again? (y or n)')
            if replay.lower() != 'y':
                print('Thank you {}! You end the game with a balance of {}'.format(name, balance))
                return None
            elif balance <= 0 :
                print('You have no remaining balance, thank you for playing')
                return None
            
        
    
def greeting():
    print('Welcome to the game of Cups and Dice!')
    print('In this game we have six sided, ten sided and twenty sided dice')
    print('You begin the game with a balance of 100')
    name = input('Enter your name: ')
    return name

def setGoal():
    #sets goal by randomly selecting integer 0 to 100
    goal = random.randint(0,100)
    print('The goal is {}'.format(goal))
    print('If you get your goal, you will earn 10 times your bet')
    print('If your roll is within 3 of your goal, but not over, you will win 5 times your bet')
    print('If your roll is within 10 of your goal, but not over, you will win 2 times your bet')
    return goal
    
def play():
    #user selects how many of each dice they want
    six = input('How many six sided die would you like to use?')
    ten = input('How many ten sided die would you like to use?')
    twenty = input('How many twenty sided die would you like to use?')
    #calls cup class by specify how many of each dice we want to use
    c = cup(int(six), int(ten), int(twenty))
    print('Your roll is: ', c.roll())
    result = c.getSum()
    return result

def calcBalance(result, goal, bet, balance):
    if result == goal:
        balance += 10*bet
    elif result >= goal - 3 and result < goal:
        balance += 5*bet
    elif result >= goal - 10 and result < goal:
        balance += 2*bet
    return balance
    
main()
