
def main():
    maxValue = findRange()
    evens = evenInts(maxValue)
    primes = listOfPrimes(maxValue)
    res = results(evens, primes)
    showResults(res)
    
def findRange():
    #Asks user the maximum value to check for
    maxValue = int(input('What is the max value we should test?'))
    return maxValue
 
def evenInts(maxValue):
    #Enters all even numbers into a list by using modulo divison by 2 with
    #no remainder
    evens = []
    for i in range(1,maxValue+1):
        if (i%2 == 0):
            evens.append(i)
    return evens

def listOfPrimes(maxValue):
    #Creates list of primes by ruling out all numbers that are divisible
    #by any number less than that numnber itself
    primes = []
    for x in range(2, maxValue+1):
        prime = True
        for i in range(2,x):
            if (x%i==0):
                prime = False
        if prime:
            primes.append(x)
    return primes
       

def results(evens, primes):
    #A dictionary is initalized and there is a nested for loop that runs 
    #every number through as well as two primes to find primes that will
    #add to give us the sum of the even. Once found they are added to the 
    #dictionary
    res = {}
    for x in evens:
        for a in primes:
            for b in primes:
                if a + b == x:
                    res[x] = [a,b]
    return res
            
def showResults(res):
    #The results are printed by retreiving items from the dictionary
    for x, [a,b] in res.items():
        print(x, '=', a, '+', b)

main()
