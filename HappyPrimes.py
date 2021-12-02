
def main():
    userNum = getNum()
    prime = primeOrNo(userNum)
    happy = happyOrSad(userNum)  
    printResult(prime, happy)
    
    
def getNum():
    #This function has user enter number to test. 
    userNum = int(input('Please enter a number you would like to test:'))
    return userNum

def primeOrNo(userNum):
    #This function tests if user input number is prime by determining if
    #the number is divisible by any numbers less than the number itself
    for x in range(2, userNum):
        if (userNum % x) == 0:
            prime = False
            return prime
        else:
            prime = True
    return prime

def happyOrSad(userNum):
    #This function initalizes a list and adds the new sum of the squared
    #digit into the list. If a number repeats, than happy is returned false
    #If not, and the sum of squared digits is zero, happy is returned true
    totalList = []
    while True:
        strNum = str(userNum)
        x = 0
        for i in strNum:
            x+= (int(i)**2)
        if x == 1:
            return True
        elif x in totalList:
            return False
        totalList.append(x)
        userNum = x
        
def printResult(prime, happy):
    #When printing, the results are categorized into 4 categories: 
    #Happy Prime, Sad Prime, Happy non-prime, and sad non-prime. 
    if happy == True:
        if prime == True:
            print('Happy Prime')
        elif prime == False:
            print('Happy non-prime')
    elif happy == False:
        if prime == True:
            print('Sad Prime')
        elif prime == False:
            print('Sad non-prime')
            

      
main()
