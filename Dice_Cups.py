
#Import random class
import random 

class sixSidedDie():
    #initalizes class and sets value of roll to 0
    def __init__(self):
        self.value = 0
        
    def roll(self):
        #gets value for roll by randomly selecting integet between 1 and 6
        self.value = random.randint(1, 6)
        return (self.value)
        
    def getFaceValue(self):
        #report value of roll
        return(self.value)
        
    def __repr__(self):
        #reports type of die used
        return('SixSidedDie({})'.format(self.value))

class tenSidedDie(sixSidedDie):
    #Import 6 sided die class, but changes int range from 1 to 10
    def roll(self):
        self.value = random.randint(1, 10)
        return(self.value)
    
    def __repr__(self):
        #Identifies die as a ten sided die
        return('TenSidedDie({})'.format(self.value))
        
class twentySidedDie(sixSidedDie):
    #import 6 sided ide class, but changes range from 1 to 20
    def roll(self):
        self.value = random.randint(1, 20)
        return(self.value)
    
    def __repr__(self):
        #identifies die as a twenty sided die
        return('TwentySidedDie({})'.format(self.value))
    
class cup():
    #initializes cup class, and sets default to one of each die
    def __init__(self, six=1, ten=1, twenty=1):
        #sum initally set to 0
        self.total = 0
        #rolls will be collected in the cup then summed.
        self.cup = []
        #for each type of die, the original classes are called and roll is simulated
        for dice in range(0,six):
            self.cup.append(sixSidedDie())
        for dice in range(0,ten):
            self.cup.append(tenSidedDie())
        for dice in range(0,twenty):
            self.cup.append(twentySidedDie())
            
    def roll(self):
        #all rolls are added to self.total and then the total is returned
        self.total = 0
        for i in self.cup:
            self.total += i.roll()
        return self.total
    
    def getSum(self):
        #returns sum of rolls
        return self.total
    
    def __repr__(self):
        #Identifies each type of die used
        return ('Cup('+','.join([str(d) for d in self.cup]) + ')')
        
