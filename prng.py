from datetime import datetime 

class WarAndPeacePseudoRandomNumberGenerator():
    def __init__(self, seed = 1000):
        self.seed = seed
        return
    
    def getSeed(self):
        seed = str(datetime.now().timestamp())
        seed = seed[-5:]
        for i in seed:
            if i == '.':
                seed = seed.replace('.', '')
        seed = int(seed)
        return seed

    def random(self):
        r = main()
        return r
        
results = []

def main(seed = 0):
    x = WarAndPeacePseudoRandomNumberGenerator()
    if seed == 0:
        seed = x.getSeed()
    file = 'war-and-peace.txt'
    charList = getChar(file, seed)
    newCharList = groupChar(charList)
    score = greaterThan(newCharList)
    r = getScore(score)
    results.append(r)
    #print(newCharList)
    #print (score)
    print(r)
    return r
    

def getChar(file, seed):
    charList = []
    x = 0 
    with open(file) as f:
        while x < 64:
            f.seek(seed)
            char = f.read(1)
            if x > 0:
                if char == charList[-1]:
                    seed = seed + 1
                    f.seek(seed)
                    char = f.read(1)
                    if char == charList[-1]:
                        seed = seed +1
                        f.seek(seed)
                        char = f.read(1)
                        charList.append(char)
                    else:
                        charList.append(char)
                else:
                    charList.append(char)
            else:
                charList.append(char)
            seed = seed + 100
            x = x + 1
    return charList

def groupChar(charList):
    n = 2
    newCharList = [(charList[i:i+n]) for i in range(0, len(charList), n)]
    return newCharList

def greaterThan(newCharList):
    score = []
    for i in newCharList:
        if i[0] > i[1]:
            score.append(1)
        elif i[0] < i[1]:
            score.append(0)
    return score
            
def getScore(score):
    r = 0
    n = 0
    for i in score:
        n = n + 1
        r = r + (i * (1/2**n))
    return r

def repeat_fun(times):
    x = WarAndPeacePseudoRandomNumberGenerator()
    for i in range(times): 
       main(x.getSeed())
    maximum = max(results)
    minimum = min(results)
    average = sum(results)/len(results)
    print('{} is the minimum value'.format(minimum))
    print('{} is the maximum value'.format(maximum))
    print('{} is the average value'.format(average))
    
#prng = WarAndPeacePseudoRandomNumberGenerator()
#prng = WarAndPeacePseudoRandomNumberGenerator(12345)
# = prng.random()
repeat_fun(10000)
